from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x600")

def show():
    myLabel = Label(root, text = clicked.get()).pack()

options = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

clicked = StringVar()
clicked.set('Days')

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_button = Button(root, text='Show Selection', command=show).pack()
root.mainloop()