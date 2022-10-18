from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('New Window')

def open():
    top = Toplevel()
    lbl = Label(top, text = "Hello world").pack()
    btn2 = Button(top, text='Self Destruct', command=top.destroy).pack()

btn = Button(root, text = 'Open second window', command=open).pack()





mainloop()