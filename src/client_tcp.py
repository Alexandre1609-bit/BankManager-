import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    print(f"Tentative de connexion à {HOST}:{PORT}")

    client.connect((HOST, PORT))

    message = b"solde"
    client.sendall(message)

    data = client.recv(1024)

    print(f"Réponse reçu du serveur : {data.decode('utf-8')}")