class CompteBancaire:
    """
    Gère un compte bancaire via différentes méthode
    """
    def __init__(self, titulaire:str):
        self.titulaire = titulaire
        self.__solde = 0.0


    def deposer(self, montant:float):
        """Ajoute un montant au solde"""
        if montant < 0: 
            raise ValueError("Montant invalide, impossible de déposer 0 ou moins")
        self.__solde += montant
        
    def retirer(self, montant:float):
        """Retire un montant au solde"""
        if montant < 0:
            raise ValueError("Montant invalide, impossible de retirer 0 ou moins")
        if montant > self.__solde:
            raise ValueError("Solde insuffisant")
        self.__solde -= montant

    @property     
    def solde(self):
        """Affiche le solde"""
        return self.__solde
    
    def virement(self, destinataire:'CompteBancaire', montant:float):
        self.retirer(montant)
        destinataire.deposer(montant)
        


    def __str__(self):
        return f"Compte de {self.titulaire}. Solde : {self.solde}"