from Tkinter import *
import Tkinter as tk
import ttk
import tkFileDialog
from Downloader import downloader
class GUI(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        label1 = Label(master, text = "Paste youtube playlist link:")
        label1.grid(row=0, column=0)
        self.entry = Entry(master, bd=5)
        self.entry.grid(row=0, column=1)
        label2 = Label(master, text ="Choose directory to place playlist")
        label2.grid(row=1,column=0)
        self.entry2 = Entry(master, bd=5, state= "disabled")
        self.entry2.grid(row=1,column=1)
        directory = ttk.Button(master, text='/', command=self.askdirectory)
        directory.grid(row=1, column=2,)
        self.path = ""
        self.playlist = ""
        download = ttk.Button(master, text="Download", command=self.download)
        download.grid(row=2, column = 1)
        self.finished = ttk.Label(master, text="")
        self.finished.grid(row=3, column=1)

    def askdirectory(self):
        self.path = tkFileDialog.askdirectory()
        self.entry2.configure(state="normal")

        self.entry2.delete(0,END)
        self.entry2.insert(0, self.path)
        self.entry2.configure(state="disabled")

    def download(self):
        self.playlist = self.entry.get()
        downloader.dowload(self.path+"/", self.playlist)
        self.finished["text"]="All the songs in your playlist have been downloaded"



def main():
    root = Tk()
    app = GUI(root)
    root.mainloop()
if __name__ == '__main__': main()

