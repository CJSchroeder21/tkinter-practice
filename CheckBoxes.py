from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("600x600")

def show():
    my_label = Label(root, text=var.get()).pack()

def show2():
    my_label = Label(root, text=var2.get()).pack()



var = IntVar()
var2= StringVar()

c1= Checkbutton(root, text = "string variable", variable=var2, onvalue='on', offvalue='off')
c = Checkbutton(root, text = 'Do not check this.', variable = var)
c.pack()
#stringbutton comes out as selected
c1.deselect()
c1.pack()

my_label = Label(root, text=var.get()).pack()

my_label2 = Label(root, text=var2.get()).pack()

c_button = Button(root, text = 'int button', command = show).pack()
c2_button = Button(root, text = 'string button', command = show2).pack()

root.mainloop()