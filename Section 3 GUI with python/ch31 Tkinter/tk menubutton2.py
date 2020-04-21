import tkinter
from tkinter import *

win = Tk()
#Definisce dimensione della finestra
win.geometry("500x500")

mb = Menubutton(win, text="File")

mb.menu = Menu(mb)
mb["menu"] = mb.menu

x1 = IntVar()
x2 = IntVar()

mb.menu.add_checkbutton(label='open', variable=x1)
mb.menu.add_checkbutton(label='close', variable=x2)
mb.pack()


mb.grid()

win.mainloop()
