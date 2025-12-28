import tkinter as tk
from tkinter import messagebox
import socket


HOST = "127.0.0.1"
PORT = 65432

class BankGUI():

    def __init__(self, root_window):
        """C'est dans le constructeur qu'on manage Tkinter ??"""
        self.root = root_window
        self.root.title("Ma banque")
        self.root.geometry("400x300") 

        #Le solde
        self.label_info = tk.Label(root_window, text="Bienvenue", font=("Arial", 14)) 
        self.label_info.pack(pady=20)
        #pady = marge verticale externe !!

        #Zone de saisie 
        self.entry_montant = tk.Entry(root_window, font=("Arial", 12))
        self.entry_montant.pack(pady=10)

        #Les boutons
        btn_frame = tk.Frame(root_window)
        btn_frame.pack(pady=20)

        #Le bouton dépôt
        self.btn_depot = tk.Button(btn_frame, text="Déposer", command=self.action_deposer)
        self.btn_depot.pack(side=tk.LEFT, padx=10)

        #Bouton retrait 
        self.btn_retrait = tk.Button(btn_frame, text="Retirer", command=self.action_retirer)
        self.btn_retrait.pack(side=tk.LEFT, padx=10)     
    
        #Afficher le solde 
        self.btn_solde = tk.Button(root_window, text="Actualiser Solde", command=self.action_solde)
        self.btn_solde.pack(pady=5)



    def _envoyer_message(self, message_a_envoyer: str) -> str:
        """
        Méthode privée (commence par _) pour gérer la socket.
        Se connecte, envoie, reçoit, déconnecte.
        """
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((HOST, PORT))
                s.sendall(message_a_envoyer.encode('utf-8'))
                respon = s.recv(1024)
                return respon.decode('utf-8')
        except ConnectionRefusedError:
            return "Erreur : Serveur éteint ou inaccessible."
        except Exception as e:
            return f"Erreur technique : {e}"


    def action_solde(self):
        reponse = self._envoyer_message("solde")
        self.label_info.config(text=reponse, fg="blue")

    def action_deposer(self):
        montant_text = self.entry_montant.get()

        if not montant_text:
            messagebox.showwarning("Veuillez entrez un montant")
            return
        
        commande = f"deposer {montant_text}"
        reponse = self._envoyer_message(commande)
        self.label_info.config(text=reponse, fg="green")
        self.entry_montant.delete(0, tk.END)

    def action_retirer(self):
        montant = self.entry_montant.get()

        if not montant:
            messagebox.showwarning("Veuillez entrez un montant")
            return

        commande = f"retirer {montant}"
        reponse = self._envoyer_message(commande)
        
        couleur = "red" if "Erreur" in reponse else "green"
        self.label_info.config(text=reponse, fg=couleur)

        self.entry_montant.delete(0, tk.END)
 

if __name__ == "__main__":
    
    window = tk.Tk()

    app = BankGUI(window)

    window.mainloop()