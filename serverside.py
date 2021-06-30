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

#receive untuk accept connection baru/client baru 

#handle untuk handle connection