from src.compte import CompteBancaire
import pytest

@pytest.fixture
def compte_paul():
    """Crée un compte par défaut pour les tests"""
    return CompteBancaire("Paul")

def test_deposer_argent(compte_paul):

    compte_paul.deposer(100)

    assert compte_paul.solde == 100

def test_retrait_impossible(compte_paul):
    compte_paul.deposer(50)

    #On parie que ce qui suit plantera avec une ValueError
    with pytest.raises(ValueError):
        compte_paul.retirer(200)

def test_retrait_valide(compte_paul):
    """Vérifie qu'un retrait normal fonctionne"""
    
    compte_paul.deposer(100)

    compte_paul.retirer(40)

    assert compte_paul.solde == 60.0

def test_virement_valide(compte_paul):
  
    receveur = CompteBancaire("Pierre")
    compte_paul.deposer(100)

    compte_paul.virement(receveur, 30)

    assert compte_paul.solde == 70.0
    assert receveur.solde == 30.0

def test_depot_neg(compte_paul):
    with pytest.raises(ValueError):
        compte_paul.deposer(-20)