import tkinter
from tkinter import *
from tkinter import messagebox

def hello():
    messagebox.showinfo('from computer', 'hey there')

win = Tk()
#Definisce dimensione della finestra
win.geometry("500x500")

b = Button(win, text="popup", command=hello)
b.pack()


win.mainloop()
