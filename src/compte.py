import sqlite3


class CompteBancaire:
    """
    Gère un compte bancaire via différentes méthode
    """
    def __init__(self, titulaire:str):
        self.titulaire = titulaire
        self.__solde = 0.0

        with sqlite3.connect("bank.db") as con:
            cur = con.cursor()

            cur.execute("SELECT solde FROM comptes WHERE nom = ?", (self.titulaire,))
            row = cur.fetchone()

            if row: #Row est un tuple !!
                self.__solde = row[0]
            else:
                print(f"Création du compte {self.titulaire}")
                cur.execute("INSERT INTO comptes (nom, solde) VALUES (?, ?)", (self.titulaire, 0))
                con.commit()


    def deposer(self, montant:float):
        with sqlite3.connect("bank.db") as con:
            cur = con.cursor()
            """Ajoute un montant au solde"""
            if montant < 0: 
                raise ValueError("Montant invalide, impossible de déposer 0 ou moins")
            self.__solde += montant
            cur.execute("UPDATE comptes SET solde = ? WHERE nom = ?", (self.__solde, self.titulaire))
            con.commit()
            
            
    def retirer(self, montant:float):
        with sqlite3.connect("bank.db") as con:
            cur = con.cursor()
            """Retire un montant au solde"""
            if montant < 0:
                raise ValueError("Montant invalide, impossible de retirer 0 ou moins")
            if montant > self.__solde:
                raise ValueError("Solde insuffisant")
            self.__solde -= montant
            cur.execute("UPDATE comptes SET solde = ? WHERE nom = ?", (self.__solde, self.titulaire))
            con.commit()

    @property     
    def solde(self):
        """Affiche le solde"""
        return self.__solde 
    
    def virement(self, destinataire:'CompteBancaire', montant:float):
        self.retirer(montant)
        destinataire.deposer(montant)
        


    def __str__(self):
        return f"Compte de {self.titulaire}. Solde : {self.solde}"