import tkinter
from tkinter import *

win = Tk()
#Definisce dimensione della finestra
win.geometry("500x500")

frame = Frame(win)
frame.pack()
frame2 = Frame(win)
frame2.pack(side=BOTTOM)

rb = Button(frame, text="red", fg='red')
rb.pack(side=LEFT)
rb = Button(frame, text="red", fg='red')
rb.pack(side=LEFT)
rb = Button(frame, text="red", fg='red')
rb.pack(side=LEFT)

gb = Button(frame2, text="green", fg='green')
gb.pack(side=BOTTOM)


win.mainloop()
