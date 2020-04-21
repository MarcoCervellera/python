import tkinter
from tkinter import *

win = Tk()
#Definisce dimensione della finestra
win.geometry("500x500")

def nothing():
    file = Toplevel(win)
    button = Button(file, text='Do Nothing')
    button.pack()

menubar = Menu(win)

filemenu = Menu(menubar)
filemenu.add_command(label='New Window', command=nothing)
filemenu.add_command(label='New File', command=nothing)
filemenu.add_command(label='Open', command=nothing)
filemenu.add_command(label='Close', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='Save', command=nothing)
filemenu.add_command(label='Save as', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='pugger', command=nothing)
filemenu.add_command(label='close tab', command=nothing)
filemenu.add_separator()
filemenu.add_command(label='exit', command=win.quit)

menubar.add_cascade(label='File', menu=filemenu)

win.config(menu=menubar)

win.mainloop()
