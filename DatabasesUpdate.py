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
# create fun update
def update():
        conn = sqlite3.connect('address_book2.db')

        # Create a cursor
        c = conn.cursor()

        record_id = id_box.get()

        c.execute("""UPDATE addresses SET
                first_name = :first,
                last_name = :last,
                address = :address,
                city = :city,
                state = :state,
                zipcode = :zipcode
                
                WHERE oid = :oid""",
                {'first' : f_name_e.get(),
                   'last' : l_name_e.get(),
                   'address' : a_name_e.get(),
                   'city' : c_name_e.get(),
                   'state' : s_name_e.get(),
                   'zipcode' : z_name_e.get(),

                   'oid' : record_id

                }
                )

        # commit changes
        conn.commit()

        # Close Connection
        conn.close()

        editor.destroy()

# crete fun to delete a record
def delete():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book2.db')

        # Create a cursor
        c = conn.cursor()

        # commit changes
        conn.commit()

        # Close Connection
        conn.close()

        # delete record
        c.execute("DELETE from addresses WHERE oid= " + id_box.get())


        delete_box.delete(0,END)
#save in editor

# Edit fun to update record
def edit():
        global f_name_e, l_name_e, a_name_e, c_name_e, s_name_e, z_name_e, editor
        editor = Tk()
        editor.geometry("300x400")

        conn = sqlite3.connect('address_book2.db')

        c = conn.cursor()

        record_id = id_box.get()
        c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
        records = c.fetchall()


        f_name_e = Entry(editor, width=30)
        f_name_e.grid(row=0, column=1, padx=20)

        l_name_e = Entry(editor, width=30)
        l_name_e.grid(row=1, column=1)

        a_name_e = Entry(editor, width=30)
        a_name_e.grid(row=2, column=1)

        c_name_e = Entry(editor, width=30)
        c_name_e.grid(row=3, column=1)

        s_name_e = Entry(editor, width=30)
        s_name_e.grid(row=4, column=1)

        z_name_e = Entry(editor, width=30)
        z_name_e.grid(row=5, column=1)



        # create text box labels
        f_name_label_e = Label(editor, text='First Name')
        f_name_label_e.grid(row=0, column=0)

        l_name_label_e = Label(editor, text='Last Name')
        l_name_label_e.grid(row=1, column=0)

        a_name_label_e = Label(editor, text='Address')
        a_name_label_e.grid(row=2, column=0)

        c_name_label_e = Label(editor, text='City')
        c_name_label_e.grid(row=3, column=0)

        s_name_label_e = Label(editor, text='State')
        s_name_label_e.grid(row=4, column=0)

        z_name_label_e = Label(editor, text='Zipcode')
        z_name_label_e.grid(row=5, column=0)


        # Loop tru results
        for record in records:
                f_name_e.insert(0, record[0])
                l_name_e.insert(0, record[1])
                a_name_e.insert(0, record[2])
                c_name_e.insert(0, record[3])
                s_name_e.insert(0, record[4])
                z_name_e.insert(0, record[5])


        # Create submit button
        save_but = Button(editor, text='Save', command=update)
        save_but.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
        conn = sqlite3.connect('address_book2.db')

        # Create a cursor
        c = conn.cursor()


        # commit changes
        conn.commit()

        # Close Connection
        conn.close()




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
                print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + str(record[6]) + '\n'


        fetch_label = Label(root, text = print_records)
        fetch_label.grid(row=12, column=0, columnspan=2)

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

# delete box
id_box = Entry(root, width=30)
id_box.grid(row = 9, column=1)


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

# delete lable
id_box_label = Label(root, text = 'ID Number')
id_box_label.grid(row=9, column=0)

# Create submit button
sub_but = Button(root, text = 'add button to data', command = submit)
sub_but.grid(row = 6, column= 0, columnspan= 2, pady= 10, padx=10, ipadx=100)

# Create a Query button
query_btn = Button(root, text="Show record", command = query)
query_btn.grid(row=7, column=0, columnspan=2, pady= 10, padx= 10, ipadx=137)

# create delete button
delete_btn = Button(root, text="Delete ID", command = delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady= 10, padx= 10, ipadx=137)

#update button
edit_btn = Button(root, text="Edit ID", command = edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady= 10, padx= 10, ipadx=137)


# commit changes
conn.commit()

# Close Connection
conn.close()

root.mainloop()