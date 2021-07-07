import socket
import threading
import role

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = []
nicknames = []

# function

# Mengirim Urutan pemberian desk kata kunci


def Urutan(arr):
    check = 1
    for client in arr:
        client.send("Anda Urutan ke ".encode('utf-8') +
                    str(check).encode('utf-8')+"\n".encode('utf-8'))
        check += 1


# Menentukan role dan memberi kata kunci masing2 role


def kirimRole(imposName, kata):
    for client in clients:
        if (nicknames[clients.index(client)] == imposName):
            # message = "Kata Kunci Anda"+kata[0]
            client.send("Kata kunci anda : ".encode('utf-8') +
                        kata[0].encode('utf-8')+"\n".encode('utf-8'))
            # client.send(message.encode('utf-8'))
        else:
            # message = "Anda Civillian"
            client.send("Kata kunci anda : ".encode('utf-8') +
                        kata[1].encode('utf-8')+"\n".encode('utf-8'))
            # client.send("Anda Civillian\n".encode('utf-8'))


# broadcast untuk ngirim pesen ke semua client


def broadcast(message):
    for client in clients:
        client.send(message)

# handle untuk handle connection


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
            break

# receive untuk accept connection baru/client baru


def receive():
    while True:
        client, address = server.accept()
        print(f"Konek dengan {str(address)}!")

        # untuk nicknames
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname dari client adalah {nickname}!")
        broadcast(f"{nickname} tersambung dalam server!\n".encode('utf-8'))
        client.send("Terkonek dalam server \n".encode('utf-8'))

        print(nicknames)
        print(clients)

        if (len(nicknames) == 3):
            impostor = role.pickImpostor(nicknames)
            kataKunci = role.kataKunci()

            for name in nicknames:
                print("nama anda: ", name)
                if(name == impostor):
                    print("role anda: Impostor")
                    print("kata kunci anda: ", kataKunci[0])
                else:
                    print("role anda: Civillian")
                    print("kata kunci anda: ", kataKunci[1])

            kirimRole(impostor, kataKunci)
            urutan = role.shuffle(clients)
            Urutan(urutan)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server running")
receive()
