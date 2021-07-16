import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog
from tkinter import *

HOST = '127.0.0.1'
PORT = 9090


def apeloh():
    pass


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw()

        # input nickname buat ask string
        self.nickname = simpledialog.askstring(
            "Nickname", "Tulis Nickname", parent=msg)
        message = f"{self.nickname}"
        self.sock.send(message.encode('utf-8'))

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="#2E3047", padx=10, pady=10)

        self.title_label = tkinter.Label(
            self.win, text="Undercover", bg="#2E3047")
        self.title_label.config(font=("Impact", 30), fg="#4ecca3")
        self.title_label.grid(column=0, columnspan=3, row=0, pady=20)

        self.info_label = tkinter.Label(
            self.win, text="Information", bg="#2E3047")
        self.info_label.config(font=("Impact", 15), fg="#FFFFFF")
        self.info_label.grid(column=0, columnspan=3)

        self.vote_label = tkinter.Label(
            self.win, text="Vote", bg="#2E3047")
        self.vote_label.config(font=("Impact", 15), fg="#FFFFFF")
        self.vote_label.grid(column=0, columnspan=3, pady=15)

        self.player1_label = tkinter.Label(
            self.win, text="Player 1", padx=5, pady=5, fg="#FFFFFF", bg="#2E3047", font=("Impact", 12))
        self.player1_label.grid(column=0, row=3, padx=5)

        self.player2_label = tkinter.Label(
            self.win, text="Player 2", padx=5, pady=5, fg="#FFFFFF", bg="#2E3047", font=("Impact", 12))
        self.player2_label.grid(column=1, row=3, padx=5)

        self.player3_label = tkinter.Label(
            self.win, text="Player 3", padx=5, pady=5, fg="#FFFFFF", bg="#2E3047", font=("Impact", 12))
        self.player3_label.grid(column=2, row=3, padx=5)

        self.voteCount1_label = tkinter.Label(
            self.win, text="0", padx=5, pady=5, fg="#FFFFFF", bg="#2E3047", font=("Impact", 12))
        self.voteCount1_label.grid(column=0, row=4, padx=5)

        self.voteCount2_label = tkinter.Label(
            self.win, text="0", padx=5, pady=5, fg="#FFFFFF", bg="#2E3047", font=("Impact", 12))
        self.voteCount2_label.grid(column=1, row=4, padx=5)

        self.voteCount3_label = tkinter.Label(
            self.win, text="0", padx=5, pady=5, fg="#FFFFFF", bg="#2E3047", font=("Impact", 12))
        self.voteCount3_label.grid(column=2, row=4, padx=5)

        self.vote1_button = tkinter.Button(
            self.win, text="Vote", padx=5, pady=5, command=self.votePlayer1, bg="#4ccca4", fg="#FFFFFF", font=("Impact", 12))
        self.vote1_button.grid(column=0, row=5, padx=5, pady=5)

        self.vote2_button = tkinter.Button(
            self.win, text="Vote", padx=5, pady=5, command=self.votePlayer2, bg="#4ccca4", fg="#FFFFFF", font=("Impact", 12))
        self.vote2_button.grid(column=1, row=5, padx=5, pady=5)

        self.vote3_button = tkinter.Button(
            self.win, text="Vote", padx=5, pady=5, command=self.votePlayer3, bg="#4ccca4", fg="#FFFFFF", font=("Impact", 12))
        self.vote3_button.grid(column=2, row=5, padx=5, pady=5)

        self.voteStart_button = tkinter.Button(
            self.win, text="Mulai Vote", padx=5, pady=5, command=self.voteStart, bg="#4ccca4", fg="#FFFFFF", font=("Impact", 12))
        self.voteStart_button.grid(column=1, row=6, padx=5, pady=5)

        self.judul_kata_label = tkinter.Label(
            self.win, text="Kata Kunci Anda", bg="#2E3047")
        self.judul_kata_label.config(font=("Impact", 15), fg="#FFFFFF")

        self.judul_kata_label.grid(column=0, columnspan=3, pady=5)
        self.kata_label = tkinter.Label(
            self.win, text=" ", bg="#2E3047")
        self.kata_label.config(font=("Impact", 20), fg="#FFFFFF")
        self.kata_label.grid(column=0, columnspan=3, pady=15)

        self.chat_label = tkinter.Label(self.win, text="Chat", bg="#2E3047")
        self.chat_label.config(font=("Impact", 15), fg="#FFFFFF")
        self.chat_label.grid(column=0, columnspan=3)

        self.text_area = tkinter.scrolledtext.ScrolledText(
            self.win, bg="#cdd1f7", height=10)
        self.text_area.config(state='disabled')
        self.text_area.grid(column=0, columnspan=3)

        self.msg_label = tkinter.Label(self.win, text="Message", bg="#2E3047")
        self.msg_label.config(font=("Impact", 12), fg="#FFFFFF")
        self.msg_label.grid(column=0, columnspan=3)

        self.input_area = tkinter.Text(self.win, height=3, bg="#cdd1f7")
        self.input_area.grid(column=0, columnspan=3)

        self.send_button = tkinter.Button(
            self.win, text="Send", command=self.write, bg="#4ccca4")
        self.send_button.config(font=("Impact", 12), fg="#FFFFFF")
        self.send_button.grid(column=0, columnspan=3, padx=20, pady=10)

        self.start_button = tkinter.Button(
            self.win, text="Start", command=self.start,  bg="#4ccca4")
        self.start_button.config(font=("Impact", 12), fg="#FFFFFF")
        self.start_button.grid(column=0, columnspan=3, padx=20, pady=10)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)

        self.win.mainloop()

    def start(self):
        message = "start\n"
        self.sock.send(message.encode('utf-8'))

    def voteStart(self):
        message = "Vote Starting\n"
        self.sock.send(message.encode('utf-8'))

    def votePlayer1(self):
        message = "VotePlayer1\n"
        self.sock.send(message.encode('utf-8'))

    def votePlayer2(self):
        message = "VotePlayer2\n"
        self.sock.send(message.encode('utf-8'))

    def votePlayer3(self):
        message = "VotePlayer3\n"
        self.sock.send(message.encode('utf-8'))

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
                mes = message.decode('utf-8')

                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                    print(self.nickname)

                elif(mes[:4] == "Kata"):
                    self.kata_label["text"] = mes[18:-1]

                elif(mes[:7] == 'player0'):
                    split = mes.split("\n")
                    if(split[0][:7] == 'player0'):
                        self.player1_label["text"] = split[0][7:]
                    if(split[1][:7] == 'player1'):
                        self.player2_label["text"] = split[1][7:]
                    if(split[2][:7] == 'player2'):
                        self.player3_label["text"] = split[2][7:]

                elif(mes[:15] == "JmlhVotePlayer0"):
                    split = mes.split("\n")
                    if(split[0][:15] == 'JmlhVotePlayer0'):
                        self.voteCount1_label["text"] = split[0][15:]
                    if(split[1][:15] == 'JmlhVotePlayer1'):
                        self.voteCount2_label["text"] = split[1][15:]
                    if(split[2][:15] == 'JmlhVotePlayer2'):
                        self.voteCount3_label["text"] = split[2][15:]

                elif(mes[:6] == "Winner"):
                    self.sock.send("pesan : ".encode('utf-8') +
                                   mes.encode('utf-8')+"\n".encode('utf-8'))
                    self.info_label["text"] = mes[7:-1]

                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', mes)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("error")
                self.sock.close()
                break


client = Client(HOST, PORT)
