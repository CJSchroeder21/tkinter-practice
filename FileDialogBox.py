from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()


def open():
    global my_imange
    root.filename = filedialog.askopenfilename(initialdir='E:/Pics', title='select file',
                                               filetypes=(('png', '*.png'), ('all files', '')))
    my_label = Label(root, text=root.filename).pack()
    my_imange = ImageTk.PhotoImage(Image.open(root.filename))
    my_imange_label = Label(image=my_imange).pack()

my_btn = Button(root, text="open files", command=open).pack()

root.mainloop()