import socket
import threading

#Connection
host = "127.0.0.1"
port = 55555

#Démarrage du serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

#Listes des clients et leurs surnoms
clients = []
nicknames = []

#Diffuser les messages à chaque client connecté
def diffuse(message):
    for client in clients:
        client.send(message)

#Traitement des messages des clients
def handle(client):
    while True:
        try:
            #Diffusion du message
            message = client.recv(1024)
            diffuse(message)
        except:
            # Suppression et fermeture de clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            diffuse(f"{nickname} left".encode("utf-8"))
            nicknames.remove(nickname)
            break

#fonction de reception / ecoute
def receive():
    while True:
        #Accès connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        #Demande et sauvegarde du surnom
        client.send(b"NICK")
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        #Affichage et diffusion du surnom
        print(f"Nickname is {nickname}")
        diffuse(f"{nickname} joined!".encode("utf-8"))
        client.send(b"Connected to server!")

        #Démarrage du fil
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
