import socket

HOST = "127.0.0.1"
PORT = 65432


print("### TERMINAL BANCAIRE ###")
print("Commande : solde | deposer X | retiquer X | quit")

while True:

    commande = input("Banque > ")

    if commande == "quit":
        break

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(commande.encode('utf-8'))


        data = client.recv(1024)
        print(f"Réponse reçu du serveur : {data.decode('utf-8')}")

print("Fermeture du terminal.")