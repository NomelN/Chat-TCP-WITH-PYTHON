import socket
import threading
from server import host, port

#choix du surnom
nickname = input("Choose your nickname: ")

#Connection au serveur
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

#Ecoute du serveur
def receive():
    while True:
        try:
            #Reception des messages du serveur
            message = client.recv(1024).decode("utf-8")
            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            #Fermeture de la connection si y'a erreur
            print("An error connection")
            client.close()
            break

#Envoi de messages au serveur
def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode("utf-8"))

#Démarrage du fil pour l'écoute et l'envoi de message
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
