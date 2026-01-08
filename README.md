# BankManager (v2.0)

Une application bancaire implémentant une architecture Client-Serveur, la Persistance des données et une chaîne CI.

Ce projet démontre l'application des principes Clean Code, SOLID et des standards DevOps.

## Fonctionnalités Clés

### Architecture Technique
* **Architecture 3-Tiers** : Séparation claire entre Client, Serveur et Données.
* **Réseau TCP** : Communication via Sockets bruts (sans framework) pour comprendre les fondations du web.
* **Persistance SQL** : Stockage durable via SQLite (l'argent survit au redémarrage).
* **Protocole Custom** : Parsing manuel des commandes (`DEPOSER`, `RETIRER`, `SOLDE`).

### Qualité & DevOps
* **CI Pipeline** : Tests automatiques lancés par GitHub Actions à chaque push.
* **Tests Unitaires** : Utilisation de `pytest` avec Fixtures pour simuler la base de données.
* **Clean Code** : Guard Clauses, Type Hinting, et Pattern Active Record simplifié.

## Installation et Démarrage

### 1. Pré-requis
Cloner le projet et installer les dépendances de test :

```bash
git clone (https://github.com/Alexandre1609-bit/BankManager-.git)
cd BankManager
pip install pytest
```

### 2. Initialiser la Base de Données (Une seule fois)

Avant de lancer le serveur, il faut créer le fichier de stockage `bank.db` :

```bash
python src/init_db.py
# Output: Base de données initialisée.
```

### 3. Lancer le Serveur (Terminal 1)

Le serveur écoute sur le port `65432` et gère les transactions.

```bash
python src/server_tcp.py
# En attente de connexion...
```

### 4. Lancer le Client (Terminal 2)

Ouvrez un nouveau terminal pour interagir avec votre banque.

```bash
python src/client_tcp.py
```

**Commandes disponibles dans le terminal bancaire :**

* `solde` : Affiche votre solde actuel.
* `deposer 50` : Dépose 50€.
* `retirer 20` : Retire 20€.
* `quit` : Quitter.

## Tests Automatisés

Le projet contient une suite de tests qui vérifie la logique métier et la persistance des données sans corrompre la vraie base (grâce aux Fixtures).

```bash
python -m pytest
```

## Structure du Projet

```text
.
├── .github/workflows/   # Configuration CI/CD (GitHub Actions)
├── src/
│   ├── compte.py        # Logique Métier + ORM (Lien SQL)
│   ├── server_tcp.py    # Serveur (Sockets & Parsing)
│   ├── client_tcp.py    # Client (Interface Console)
│   └── init_db.py       # Script d'initialisation BDD
├── tests/
│   └── test_compte.py   # Tests avec Fixtures SQLite
└── README.md

```

Réalisé par Alexnandre
