#!/usr/bin/env python3
"""
Token Forge CrewAI - Script principal
Ce script orchestre l'équipe d'agents IA pour développer une plateforme de création de tokens ERC-20.
"""

import os
import yaml
import dotenv
from pathlib import Path
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from crewai.tasks.task_output import TaskOutput

# Chargement des variables d'environnement
dotenv.load_dotenv()

# Chemin vers les fichiers de configuration
CONFIG_DIR = Path("config")
TASK_SAVE_DIR = Path("task_save")

def load_yaml(file_path):
    """Charge un fichier YAML et retourne son contenu."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def get_llm(config):
    """Crée une instance LLM basée sur la configuration."""
    llm_type = config.get('llm_type')
    model_name = config.get('model_name')
    temperature = config.get('temperature', 0.7)
    
    if llm_type == 'openai':
        return ChatOpenAI(
            model=model_name,
            temperature=temperature,
            api_key=os.getenv('OPENAI_API_KEY')
        )
    elif llm_type == 'anthropic':
        return ChatAnthropic(
            model=model_name,
            temperature=temperature,
            api_key=os.getenv('ANTHROPIC_API_KEY')
        )
    elif llm_type == 'google':
        return ChatGoogleGenerativeAI(
            model=model_name,
            temperature=temperature,
            api_key=os.getenv('GOOGLE_API_KEY')
        )
    elif llm_type == 'groq':
        return ChatGroq(
            model=model_name,
            temperature=temperature,
            api_key=os.getenv('GROQ_API_KEY')
        )
    else:
        raise ValueError(f"LLM type {llm_type} not supported")

def create_agents():
    """Crée les agents à partir des fichiers de configuration YAML."""
    agents = {}
    agents_config = load_yaml(CONFIG_DIR / "agents.yaml")
    
    for agent_id, agent_config in agents_config.items():
        llm = get_llm(agent_config['llm'])
        
        agents[agent_id] = Agent(
            role=agent_config['role'],
            goal=agent_config['goal'],
            backstory=agent_config['backstory'],
            verbose=agent_config.get('verbose', True),
            allow_delegation=agent_config.get('allow_delegation', True),
            llm=llm
        )
    
    return agents

# Définir une fonction de callback qui écrit l'output dans un fichier
def make_sauvegarder_callback(nom_fichier: str):
    def sauvegarder_resultat(output: TaskOutput):
        # Ouvre le fichier en mode ajout pour ne pas écraser les précédents
        with open(TASK_SAVE_DIR/nom_fichier, "a", encoding="utf-8") as f:
            f.write(output.raw + "\n\n")  # output.raw contient le texte brut de la tâche
    return sauvegarder_resultat

def create_tasks(agents):
    """Crée les tâches à partir des fichiers de configuration YAML."""
    tasks = []
    tasks_config = load_yaml(CONFIG_DIR / "tasks.yaml")
    
    for task_id, task_config in tasks_config.items():
        agent_id = task_config['agent']
        
        name = task_config['name']
        tasks.append(Task(
            description=task_config['description'],
            agent=agents[agent_id],
            expected_output=task_config['expected_output'],
            output_file=task_config.get('output_file'),
            callback=make_sauvegarder_callback(f"{name}.txt")
        ))
    return tasks


def main():
    """Fonction principale qui orchestre l'exécution de l'équipe."""
    print("🚀 Initialisation du projet Token Forge avec CrewAI")
    
    # Création des agents
    print("👥 Création des agents spécialisés...")
    agents = create_agents()
    
    # Création des tâches
    print("📝 Création des tâches...")
    tasks = create_tasks(agents)
    
    
    # Création du processus (depuis la configuration)
    crew_config = load_yaml(CONFIG_DIR / "crew.yaml")
    process_type = Process.hierarchical if crew_config.get('process') == 'hierarchical' else Process.sequential
    
  
    # Configurer les paramètres de Crew en fonction du type de processus
    crew_kwargs = {
        'tasks': tasks,
        'verbose': crew_config.get('verbose', True),
        'process': process_type,
        'output_log_file': crew_config.get('output_log_file')
    }
    
    # En mode hiérarchique, extraire le manager et mettre les autres agents dans la liste
    if process_type == Process.hierarchical:
        manager_agent = agents.get('project_manager')
        if manager_agent:
            # Retirer le manager de la liste des agents
            regular_agents = [agent for agent_id, agent in agents.items() if agent_id != 'project_manager']
            crew_kwargs['agents'] = regular_agents
            crew_kwargs['manager_agent'] = manager_agent
        else:
            # Si pas de manager défini, utiliser tous les agents normalement
            crew_kwargs['agents'] = list(agents.values())
    else:
        # En mode séquentiel, utiliser tous les agents
        crew_kwargs['agents'] = list(agents.values())
    
    # Création de l'équipe
    print("🛠️ Formation de l'équipe Token Forge...")
    token_forge_crew = Crew(**crew_kwargs)

    # Exécution de l'équipe
    print("🏁 Démarrage du travail d'équipe...")
    result = token_forge_crew.kickoff()

    print(result.raw) # Afficher le résultat de l'exécution

    # Enregistrer dans un fichier
    with open('crew_output.txt', 'w', encoding='utf-8') as f:
        f.write(str(result.raw))

    print("Résultat enregistré dans crew_output.txt")

if __name__ == "__main__":
    main()