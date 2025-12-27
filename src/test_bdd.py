from compte import CompteBancaire
import sqlite3

print("--- TEST DE CHARGEMENT ---")


paul = CompteBancaire("Paul") 

print(f"Solde de Paul (Attendu: 100.0) : {paul.solde}")

print("\n--- TEST DE CRÉATION ---")


nouveau = CompteBancaire("NouveauClient")
print(f"Solde Nouveau (Attendu: 0.0) : {nouveau.solde}")


with sqlite3.connect("bank.db") as con:
    cur = con.cursor()
    cur.execute("SELECT nom FROM comptes WHERE nom = 'NouveauClient'")
    resultat = cur.fetchone()
    
    if resultat:
        print("SUCCÈS : Le nouveau client a bien été enregistré dans la BDD !")
    else:
        print("ÉCHEC : Le client n'est pas dans la base (problème de commit ?)")