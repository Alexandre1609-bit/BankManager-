# Bank Account Manager

Un projet Python simple démontrant l'application des principes de Clean Code, de la POO et des Tests Unitaires.

## Objectifs du projet

Ce projet est une simple simulation bancaire, visant à apprendre à implémenter des standards professionnels de développement :

* **Encapsulation stricte** : Usage d'attributs privés et de décorateurs `@property`.
* **Défense en profondeur** : Utilisation de "Guard Clauses" pour la validation des données.
* **Principe DRY** (Don't Repeat Yourself) : Réutilisation de logique pour les virements.
* **Tests Automatisés** : Couverture de tests avec `pytest` et usage de *fixtures*.
* **Type Hinting** : Typage statique pour la robustesse du code.

## Installation et Utilisation

1.  **Cloner le projet**
    ```bash
    git clone (https://github.com/Alexandre1609-bit/BankManager-.git)
    cd BankManager
    ```

2.  **Lancer les tests (Recommandé)**
    Le projet contient une suite de tests complète.
    ```bash
    # Installer pytest si nécessaire
    pip install pytest

    # Lancer les tests
    python -m pytest
    ```

## Structure du code

* `compte.py` : La classe métier contenant la logique (Dépôt, Retrait, Virement).
* `tests/` : Dossier contenant les tests unitaires.

## Exemple d'usage

```python
from compte import CompteBancaire

# Création
paul = CompteBancaire("Paul")
paul.deposer(100)

# Virement sécurisé
pierre = CompteBancaire("Pierre")
paul.virement(pierre, 30)

print(paul) # "Compte de Paul. Solde : 70.0"
```