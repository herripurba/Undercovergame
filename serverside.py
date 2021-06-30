import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []

#function

#broadcast untuk ngirim pesen ke semua client
def broadcast(message):
    for client in clients:
        client.send(message)

#handle untuk handle connection
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)

#receive untuk accept connection baru/client baru 
def receive():
    while True:
        client, address = server.accept()
        print(f"Konek dengan {str(address)}!")

        #untuk nicknames
        client.send("NICK".encode('utf-8'))
        nickname = client.receive(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname dari client adalah {nickname}!")
        broadcast(f"{nickname} ter-Konek dalam server!\n".encode('utf-8'))
        client.send("Terkonek dalam server".encode('utf-8'))

        thread = threading.Thread(target=handle, args = (client,))
        thread.start()
