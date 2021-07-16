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
votes = []
chanceVotes = []
impostors = []
stateVote = []
gameStart = [0]

# function

# Mengecek Pemenang


def checkWinner():
    voteTerbesar = max(votes)
    print(nicknames[votes.index(voteTerbesar)])
    if(nicknames[votes.index(voteTerbesar)] == impostors[0]):
        print("masok")
        for client in clients:
            client.send("Winner Civillian Win\n".encode('utf-8'))
    else:
        for client in clients:
            client.send("Winner Impostor Win\n".encode('utf-8'))


# Mengirim jumlah votedari tiap tiap pemain ke semua server

def sendJumlahVote():
    for client in clients:
        message = "JmlhVotePlayer0".encode('utf-8')+str(votes[0]).encode('utf-8')+"\n".encode('utf-8')+"JmlhVotePlayer1".encode('utf-8')+str(
            votes[1]).encode('utf-8')+"\n".encode('utf-8')+"JmlhVotePlayer2".encode('utf-8')+str(votes[2]).encode('utf-8')+"\n".encode('utf-8')
        client.send(message)


# Fungsi untuk mengirim list nicknames ke client

def kirimNicnames(num):
    for client in clients:
        tes = clients[num]
        message = "player".encode(
            'utf-8')+str(num).encode('utf-8')+nicknames[clients.index(tes)]+"\n".encode('utf-8')
        client.send(message)


# Menentukan role dan memberi kata kunci masing2 role

def kirimRole(imposName, kata):
    impostors.append(imposName)
    stateVotes = 0
    stateVote.append(stateVotes)
    gameStart[0] = 1
    for client in clients:
        if (nicknames[clients.index(client)] == imposName):
            client.send("Kata kunci anda : ".encode('utf-8') +
                        kata[0].encode('utf-8')+"\n".encode('utf-8'))
        else:
            client.send("Kata kunci anda : ".encode('utf-8') +
                        kata[1].encode('utf-8')+"\n".encode('utf-8'))
    print(impostors[0], type(impostors[0]))


# broadcast untuk ngirim pesen ke semua client

def broadcast(message):
    for client in clients:
        client.send(message)


# handle untuk handle connection

def handle(client):

    while True:
        try:
            message = client.recv(1024)
            mes = message.decode('utf-8')
            firstNic = nicknames[0]
            print(f"{nicknames[clients.index(client)]} says {message}")

            # Start game
            if(mes[:5] == "start" and len(nicknames) >= 3 and firstNic == nicknames[clients.index(client)] and gameStart[0] == 0):
                print("Berhasil")
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
                for num in range(len(nicknames)):
                    kirimNicnames(num)

            # check jika menekan tombol voting dan game belum mulai
            elif(mes[:13] == "Vote Starting" and (firstNic != nicknames[clients.index(client)] or firstNic == nicknames[clients.index(client)]) and gameStart[0] == 0):
                pesan = "Harap Start Game Terlebih dahulu\n"
                client.send(pesan.encode('utf-8'))

            # Memulai voting oleh palyer pertama
            elif(mes[:13] == "Vote Starting" and len(nicknames) >= 3 and firstNic == nicknames[clients.index(client)] and stateVote[0] == 0 and gameStart[0] == 1):
                stateVote[0] = 1

            # Mengecek yang menekan mulai voting jika bukan player pertama
            elif(mes[:13] == "Vote Starting" and len(nicknames) >= 3 and firstNic != nicknames[clients.index(client)] and stateVote[0] == 0 and gameStart[0] == 1):
                pesan = "Hanya player 1 yang dapat memulai Vote\n"
                client.send(pesan.encode('utf-8'))

            # Mengecek jumlah pemain untuk memulai game
            elif(mes[:5] == "start" and len(nicknames) < 3 and firstNic == nicknames[clients.index(client)] and gameStart[0] == 0):
                pesan = "Pemain masih kurang dari 3 pemain\n"
                client.send(pesan.encode('utf-8'))

            # Mengecek yang menekan tombol start jika bukan player 1
            elif(mes[:5] == "start" and firstNic != nicknames[clients.index(client)] and gameStart[0] == 0):
                pesan = "Hanya player 1 yang dapat memulai game\n"
                client.send(pesan.encode('utf-8'))

            # Menghitung jumlah orang yang sudah melakukan vote agar tidak dapat memvote lagi jika jumlahnya sudah sesuai banyak pemain
            elif(sum(votes) >= 3):
                pesan = "Tidak dapat melakukan vote lagi\n"
                client.send(pesan.encode('utf-8'))

            # Mengecek jika pemain menekan tombol vote dan game belum dimulai
            elif((mes[:11] == "VotePlayer1" or mes[:11] == "VotePlayer2" or mes[:11] == "VotePlayer3") and gameStart[0] == 0):
                mess = "Harap Start Game Terlebih Dahulu\n"
                client.send(mess.encode('utf-8'))

            # Menambahkan vote pada player yang tombol votenya ditekan dan mengurangi kesempatan player yang menekan melakukan vote lagi
            elif(clients.index(client) != 0 and mes[:11] == "VotePlayer1" and sum(votes) < 3 and chanceVotes[clients.index(client)] == 1 and stateVote[0] == 1 and gameStart[0] == 1):
                chanceVotes[clients.index(
                    client)] = chanceVotes[clients.index(client)]-1
                votes[0] = votes[0]+1
                print("masuk1")
                sendJumlahVote()
                if(sum(votes) == 3):
                    checkWinner()

            # Menambahkan vote pada player yang tombol votenya ditekan dan mengurangi kesempatan player yang menekan melakukan vote lagi
            elif(clients.index(client) != 1 and mes[:11] == "VotePlayer2" and sum(votes) < 3 and chanceVotes[clients.index(client)] == 1 and stateVote[0] == 1 and gameStart[0] == 1):
                chanceVotes[clients.index(
                    client)] = chanceVotes[clients.index(client)]-1
                votes[1] = votes[1]+1
                print("masuk1")
                sendJumlahVote()
                if(sum(votes) == 3):
                    checkWinner()

            # Menambahkan vote pada player yang tombol votenya ditekan dan mengurangi kesempatan player yang menekan melakukan vote lagi
            elif(clients.index(client) != 2 and mes[:11] == "VotePlayer3" and sum(votes) < 3 and chanceVotes[clients.index(client)] == 1 and stateVote[0] == 1 and gameStart[0] == 1):
                chanceVotes[clients.index(
                    client)] = chanceVotes[clients.index(client)]-1
                votes[2] = votes[2]+1
                print("masuk1")
                sendJumlahVote()
                if(sum(votes) == 3):
                    checkWinner()

            # Mengecek jika pemain tersebut menekan tombol votenya sendiri
            elif(clients.index(client) == 0 and mes[:11] == "VotePlayer1" and gameStart[0] == 1):
                mess = "Anda tidak dapat memvote anda sendiri\n"
                client.send(mess.encode('utf-8'))

            # Mengecek jika pemain tersebut menekan tombol votenya sendiri
            elif(clients.index(client) == 1 and mes[:11] == "VotePlayer2" and gameStart[0] == 1):
                mess = "Anda tidak dapat memvote anda sendiri\n"
                client.send(mess.encode('utf-8'))

            # Mengecek jika pemain tersebut menekan tombol votenya sendiri
            elif(clients.index(client) == 2 and mes[:11] == "VotePlayer3" and gameStart[0] == 1):
                mess = "Anda tidak dapat memvote anda sendiri\n"
                client.send(mess.encode('utf-8'))

            # Mengecek apakah pemain tersebut sudah melakukan vote dan tidak diberikan kesempatan memvote lagi
            elif(chanceVotes[clients.index(client)] == 0 and gameStart[0] == 1):
                mess = "Anda tidak dapat melakukan vote lagi\n"
                client.send(mess.encode('utf-8'))

            # Mengecek jika menekan tombol vote sedangkan player 1 belum menekan tombol mulai vote
            elif(stateVote[0] == 0 and (mes[:11] == "VotePlayer1" or mes[:11] == "VotePlayer2" or mes[:11] == "VotePlayer3") and gameStart[0] == 1):
                mess = "Vote belom dimulai\n"
                client.send(mess.encode('utf-8'))

            else:
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
        a = 0
        chanceVote = 1

        nicknames.append(nickname)
        clients.append(client)
        votes.append(a)
        chanceVotes.append(chanceVote)

        print(f"Nickname dari client adalah {nickname}!")
        broadcast(f"{nickname} tersambung dalam server!\n".encode('utf-8'))
        client.send("Tersambung dalam server \n".encode('utf-8'))

        print(nicknames)
        print(clients)

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server running")
receive()
