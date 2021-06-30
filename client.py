import socket 
import threading
import tkinter
import tkinter.scrolledtext 
from tkinter import simpledialog

HOST = '127.0.0.1'
PORT = 9090

class Client:
    def __init__(self, host , port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()

        #input nickname buat ask string
        self.nickname = simpledialog.askstring("Nickname", "Tulis Nickname", parent=msg)

        self.gui_done = False
        