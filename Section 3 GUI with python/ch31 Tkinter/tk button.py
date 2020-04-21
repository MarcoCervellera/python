import tkinter
from tkinter import *

def pr():
    print('hi')

win = Tk()
#Definisce dimensione della finestra
win.geometry("500x500")
#definizione del bottone
b = Button(win, text="button", command=pr, padx=50, pady=50, activeforeground="red")
#il metodo pack mostra il bottone
#b.pack()
#grid imposta la finestra come una griglia
#b.grid(row=1, column=2)
#place inserisce l'elemento dove desiderato
b.place(x=100, y=200)

b2 = Button(win, text="bu")
#il metodo pack mostra il bottone
#b2.grid(row=1, column=1)
b2.place(x=300, y=200)

win.mainloop()
