import pytest
import sqlite3
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from compte import CompteBancaire


@pytest.fixture(autouse=True)
def setup_database():
    """
    Cette fonction s'exécute automatiquement AVANT et APRÈS chaque test.
    """
    
    with sqlite3.connect("bank.db") as con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS comptes") 
        cur.execute("""
            CREATE TABLE comptes (
                nom TEXT PRIMARY KEY,
                solde REAL NOT NULL
            );
        """)
        
        cur.execute("INSERT INTO comptes (nom, solde) VALUES (?, ?)", ("TestUser", 100.0))
        con.commit()

    yield 

    if os.path.exists("bank.db"):
        os.remove("bank.db")

def test_creation_compte_existant():
    """Vérifie qu'on récupère bien le solde de la BDD"""
    compte = CompteBancaire("TestUser") 
    assert compte.solde == 100.0

def test_creation_nouveau_compte():
    """Vérifie la création d'un nouveau client"""
    compte = CompteBancaire("Nouveau")
    assert compte.solde == 0.0
    
    with sqlite3.connect("bank.db") as con:
        cur = con.cursor()
        cur.execute("SELECT solde FROM comptes WHERE nom = 'Nouveau'")
        assert cur.fetchone() is not None

def test_depot():
    compte = CompteBancaire("TestUser")
    compte.deposer(50.0)
    
    assert compte.solde == 150.0
    
    with sqlite3.connect("bank.db") as con:
        cur = con.cursor()
        res = cur.execute("SELECT solde FROM comptes WHERE nom = 'TestUser'").fetchone()
        assert res[0] == 150.0

def test_retrait_erreur():
    compte = CompteBancaire("TestUser")
    with pytest.raises(ValueError):
        compte.retirer(200.0)