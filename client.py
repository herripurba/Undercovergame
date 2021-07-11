import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
from tkinter import *

HOST = '127.0.0.1'
PORT = 9090


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()

        # input nickname buat ask string
        self.nickname = simpledialog.askstring(
            "Nickname", "Tulis Nickname", parent=msg)

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="#2E3047",padx=10, pady=10)
        

        self.vote_label = tkinter.Label(self.win, text="Undercover", bg="#2E3047")
        self.vote_label.config(font=("Impact", 12), fg="#4ecca3")
        # self.chat_label.pack(padx=20, pady=5)
        self.vote_label.grid(column=0, columnspan=4, row= 0)

        self.player1_label = tkinter.Label(self.win, text="Player 1", padx=5, pady=5, fg="#FFFFFF", bg="#2E3047", font=("Impact", 12))
        self.player1_label.grid(column=0, row= 1, padx=5)

        self.player2_label = tkinter.Label(self.win, text="Player 2", padx=5, pady=5, fg="#FFFFFF", bg="#2E3047", font=("Impact", 12))
        self.player2_label.grid(column=1, row= 1, padx=5)

        self.player3_label = tkinter.Label(self.win, text="Player 3", padx=5, pady=5, fg="#FFFFFF", bg="#2E3047", font=("Impact", 12))
        self.player3_label.grid(column=2, row= 1, padx=5)
        
        self.vote1_button = tkinter.Button(self.win, text="Player 1", padx=5, pady=5, bg="#4ccca4", fg="#FFFFFF", font=("Impact", 12))
        self.vote1_button.grid(column=0, row= 2, padx=5, pady=5)

        self.vote2_button = tkinter.Button(self.win, text="Player 2", padx=5, pady=5, bg="#4ccca4", fg="#FFFFFF", font=("Impact", 12))
        self.vote2_button.grid(column=1, row= 2, padx=5, pady=5)

        self.vote3_button = tkinter.Button(self.win, text="Player 3", padx=5, pady=5, bg="#4ccca4", fg="#FFFFFF", font=("Impact", 12))
        self.vote3_button.grid(column=2, row= 2, padx=5, pady=5)

        self.chat_label = tkinter.Label(self.win, text="Chat", bg="#2E3047")
        self.chat_label.config(font=("Impact", 12), fg="#FFFFFF")
        # self.chat_label.pack(padx=20, pady=5)
        self.chat_label.grid(column=0, columnspan=3)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win, bg="#cdd1f7", height=10)
        # self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled')
        self.text_area.grid(column=0, columnspan=3)

        self.msg_label = tkinter.Label(self.win, text="Message", bg="#2E3047")
        self.msg_label.config(font=("Impact", 12), fg="#FFFFFF")
        # self.msg_label.pack(padx=20, pady=5)
        self.msg_label.grid(column=0, columnspan=3)

        self.input_area = tkinter.Text(self.win, height=3, bg="#cdd1f7")
        # self.input_area.pack(padx=20, pady=5)
        self.input_area.grid(column=0, columnspan=3)

        self.send_button = tkinter.Button(
            self.win, text="Send", command=self.write, bg="#4ccca4")
        self.send_button.config(font=("Impact", 12), fg="#FFFFFF")
        # self.send_button.pack(padx=20, pady=5)
        self.send_button.grid(column=0, columnspan=3, padx=20, pady=10)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    def write(self):
        message = f"{self.nickname}: {self.input_area.get('1.0', 'end')}"
        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0', 'end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024)
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                    print(self.nickname)
                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("error")
                self.sock.close()
                break


client = Client(HOST, PORT)
