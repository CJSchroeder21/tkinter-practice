from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("600x600")

def slide():
    my_lab = Label(root, text=str(horizontal.get()) + ' wide/ ' + str(vertical.get())).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=200, to=600)
vertical.pack()

horizontal = Scale(root, from_=200, to=600, orient=HORIZONTAL)
horizontal.pack()




my_but = Button(root, text="click me", command=slide).pack()
root.mainloop()