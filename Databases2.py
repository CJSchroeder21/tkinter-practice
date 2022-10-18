from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.geometry("600x600")

# Create a database or connect to one
conn = sqlite3.connect('address_book2.db')

# Create a cursor
c = conn.cursor()

# Create table
'''
c.execute("""CREATE TABLE addresses (
        first_name text, 
        last_name text,
        address text,
        city text,
        state text,
        zip interger
        )""")
'''
#create submit fuction for data
def submit():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book2.db')

        # Create a cursor
        c = conn.cursor()


        # Insert into table
        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :a_name, :c_name, :s_name, :z_name)",
                {
                        'f_name' : f_name.get(),
                        'l_name': l_name.get(),
                        'a_name': a_name.get(),
                        'c_name': c_name.get(),
                        's_name': s_name.get(),
                        'z_name' : z_name.get()

                })
        # commit changes
        conn.commit()

        # Close Connection
        conn.close()

        f_name.delete(0, END)
        l_name.delete(0, END)
        a_name.delete(0, END)
        c_name.delete(0, END)
        s_name.delete(0,END)
        z_name.delete(0, END)


def query():
        global fetch_label, records
        conn = sqlite3.connect('address_book2.db')

        c = conn.cursor()

        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()

        print_records = ''
        for record in records:
                print_records += str(record) + '\n'


        fetch_label = Label(root, text = print_records)
        fetch_label.grid(row=8, column=0, columnspan=2)

        conn.commit()

        conn.close()


#Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

a_name = Entry(root, width=30)
a_name.grid(row=2, column=1)

c_name = Entry(root, width=30)
c_name.grid(row=3, column=1)

s_name = Entry(root, width=30)
s_name.grid(row=4, column=1)

z_name = Entry(root, width=30)
z_name.grid(row=5, column=1)



#create text box labels
f_name_label = Label(root, text = 'First Name')
f_name_label.grid(row=0,column=0)

l_name_label = Label(root, text = 'Last Name')
l_name_label.grid(row=1,column=0)

a_name_label = Label(root, text = 'Address')
a_name_label.grid(row=2,column=0)

c_name_label = Label(root, text = 'City')
c_name_label.grid(row=3,column=0)

s_name_label = Label(root, text = 'State')
s_name_label.grid(row=4, column=0)

z_name_label = Label(root, text = 'Zipcode')
z_name_label.grid(row=5, column=0)


# Create submit button
sub_but = Button(root, text = 'add button to data', command = submit)
sub_but.grid(row = 6, column= 0, columnspan= 2, pady= 10, padx=10, ipadx=100)

# Create a Query button
query_btn = Button(root, text="Show record", command = query)
query_btn.grid(row=7, column=0, columnspan=2, pady= 10, padx= 10, ipadx=137)

# commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()