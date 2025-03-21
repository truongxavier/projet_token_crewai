# Token Forge CrewAI

Un projet utilisant CrewAI pour développer une plateforme de création de tokens ERC-20 sur la blockchain Ethereum.

## Description du projet

Token Forge est une plateforme permettant à quiconque de créer et lancer facilement son propre token ERC-20 sur la blockchain Ethereum. Ce projet utilise CrewAI pour orchestrer une équipe d'agents IA spécialisés, chacun ayant un rôle spécifique dans le développement de la plateforme.

## Structure du projet

L'équipe CrewAI est composée de plusieurs agents spécialisés, chacun utilisant un modèle de langage adapté à sa spécialité :

1. **Chef de Projet Blockchain** (Claude 3 Opus)
   - Coordonne l'équipe et assure la réussite globale du projet
   - Établit le plan de projet et gère les dépendances entre tâches

2. **Expert Solidity et Développeur ERC-20** (GPT-4o)
   - Développe les contrats ERC-20 de base
   - Implémente les fonctionnalités avancées (burning, minting, etc.)

3. **Expert en Patterns de Design pour Contrats Intelligents** (Claude 3 Opus)
   - Conçoit l'architecture des contrats
   - Implémente les patterns Factory et Proxy

4. **Expert en Sécurité Blockchain et Gestion des Accès** (GPT-4o)
   - Développe le système de gestion des accès
   - Assure la sécurité des contrats

5. **Expert en DEX et Pools de Liquidité** (GPT-4o)
   - Intègre les DEX pour la création de pools de liquidité
   - Optimise les mécanismes d'échange

6. **Expert en Développement Frontend pour dApps** (LLaMA3 70B)
   - Crée l'interface utilisateur de la plateforme
   - Intègre Ethers.js pour l'interaction avec la blockchain

7. **Expert en Tests et Déploiement Blockchain** (Gemini 1.5 Pro)
   - Développe les tests unitaires et d'intégration
   - Prépare les scripts de déploiement

8. **Expert en Documentation Technique Blockchain** (Claude 3 Sonnet)
   - Crée la documentation technique et les guides utilisateur
   - Explique les choix architecturaux

## Fichiers du projet

```
token-forge-crewai/
│
├── config/                      # Configuration du système
│   ├── agents.yaml              # Configuration des agents IA
│   ├── tasks.yaml               # Configuration des tâches
│   └── crew.yaml                # Configuration de l'équipe
│
├── output/                      # Dossier pour les résultats générés
│   └── results.md               # Résultats finaux (sera créé lors de l'exécution)
│
├── main.py                      # Script principal
├── requirements.txt             # Dépendances du projet
├── .env                         # Variables d'environnement (clés API)
└── README.md                    # Documentation du projet
```

## Prérequis

- Python 3.9+
- Clés API pour différents LLM (OpenAI, Anthropic, Google, Groq)

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/token-forge-crewai.git
   cd token-forge-crewai
   ```

2. Créez et activez un environnement virtuel :
   ```bash
   # Sur Windows
   python -m venv venv
   venv\Scripts\activate

   # Sur macOS et Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Configurez les variables d'environnement :
   ```bash
   cp .env.example .env
   # Modifiez le fichier .env avec vos clés API
   ```

## Utilisation

1. Exécutez le script principal :
   ```bash
   python main.py
   ```

2. Les résultats seront disponibles dans le dossier `output/`.

## Configuration

Le projet est entièrement configurable via les fichiers YAML dans le dossier `config/` :

- `agents.yaml` : Configuration des agents et de leurs modèles LLM
- `tasks.yaml` : Configuration des tâches à accomplir
- `crew.yaml` : Configuration de l'équipe et du processus

## Mode de fonctionnement hiérarchique

Le projet utilise le mode hiérarchique de CrewAI, où le Chef de Projet supervise et coordonne le travail des autres agents. Cela permet une meilleure organisation et une communication plus efficace entre les membres de l'équipe.

## Variables d'environnement requises

Créez un fichier `.env` avec les clés API nécessaires :

```
OPENAI_API_KEY=votre-clé-api-openai
ANTHROPIC_API_KEY=votre-clé-api-anthropic
GOOGLE_API_KEY=votre-clé-api-google
GROQ_API_KEY=votre-clé-api-groq
```

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.