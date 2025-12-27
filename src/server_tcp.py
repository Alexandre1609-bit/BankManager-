import socket
from compte import CompteBancaire

#Config
HOST = "127.0.0.1" #Loopback address
PORT = 65432 #port aléatoire pour pas toucher aux ports sys

#Créer le socket
#nb: AF_INET = utilisation IPv4
#SOCK_STREAM = Utilisation de TCP 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    #On lie le socket à l'adresse
    server.bind((HOST, PORT))

    #mode listening
    server.listen()
    print(f"Serveur en écoute sur {HOST}:{PORT}")
    
    compte_test = CompteBancaire("Banque")

    try:
        while True:
            print("En attente d'un client")

            #Accepter une connexion (rien ne se passe tant que personne ne se connecte)
            connexion, adresse_client = server.accept()
            
            with connexion:
                print(f"Connecté avec {adresse_client}")

                #On reçoit les données (1024 octets lac d'un coup!)
                data = connexion.recv(1024)
                #Vérification de data pour ne pas saturer de bytes vide
                if not data:
                    break
                decoded_data = data.decode('utf-8').lower().split(" ")
                try:
                    if decoded_data[0] == "solde":
                        connexion.sendall(f"Solde : {compte_test.solde}".encode('utf-8'))
                    elif decoded_data[0] == "deposer":
                        compte_test.deposer(float(decoded_data[1]))
                        connexion.sendall(b"Depot effectue avec succes.")
                    elif decoded_data[0] == "retirer":
                        compte_test.retirer(float(decoded_data[1]))
                        connexion.sendall(b"retrait effectue avec succes")
                except Exception as e:
                    message_erreur = f"Erreur : {str(e)}"
                    connexion.sendall(message_erreur.encode('utf-8'))                    
                print(f"Reçu : {data.decode('utf-8')}")

                #Réponse
                connexion.sendall(b"Message bien recu")
    except: KeyboardInterrupt
    print("Arrêt du serveur")