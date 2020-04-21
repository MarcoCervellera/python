import tkinter
from tkinter import *

win = Tk()
#Definisce dimensione della finestra
win.geometry("500x500")

lb = Listbox(win)

lb.insert(1,'python')
lb.insert(2, 'c')
lb.insert(3, 'c++')

lb.pack()


win.mainloop()
