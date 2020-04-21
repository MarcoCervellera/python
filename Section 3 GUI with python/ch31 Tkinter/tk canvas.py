import tkinter
from tkinter import *

def pr():
    print('hi')

win = Tk()

#Definizione del canvas
c = Canvas(win, height=250,width=300, bg="blue")
#aggiungiamo un child canvas
#in questo caso un arco
coord=10,50,240,210
arc = c.create_arc(coord, start=0, extent=150, fill="red")

line = c.create_line(10,10,200,200, fill="white")

c.pack()

win.mainloop()
