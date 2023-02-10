from tkinter import *

def send_data():
    username_data = username.get()
    password_data = str(password.get())
    fullname_data = fullname.get()
    age_data = str(age.get())

    print(username_data, '\t', password_data, '\t', fullname_data, '\t', age_data)

    newfile = open('Registro.txt', 'a')
    newfile.write(username_data)
    newfile.write('\t')
    newfile.write(password_data)
    newfile.write('\t')
    newfile.write(fullname_data)
    newfile.write('\t')
    newfile.write(age_data)
    newfile.write('\n')
    newfile.close()
    print('Nuevo Registro de Usuario. Username: {}  |  Fullname: {}    '.format(username_data, fullname_data) )

    username_entry.delete(0,END)
    password_entry.delete(0,END)
    fullname_entry.delete(0,END)
    age_entry.delete(0,END)

mywindow = Tk()
mywindow.geometry('650x550')
mywindow.title('Formulario de Registro | Python + Tkinter')
mywindow.resizable(False,False)
mywindow.config(background="blue")
main_title = Label(text='Formulario de Registro en Python | Alain Cervantes', font=('Cambria', 13), bg='#56CD63', fg='white', width='550', height='2' )
main_title.pack()

username_label = Label(text='Username', bg='white')
username_label.place(x=22, y=70)
password_label = Label(text='Password', bg='white')
password_label.place(x=22, y=130)
fullname_label = Label(text='Fullname', bg='white')
fullname_label.place(x=22, y=190)
age_label = Label(text='Age', bg='white')
age_label.place(x=22, y=250)

username = StringVar()
password = StringVar()
fullname = StringVar()
age = StringVar()

username_entry = Entry(textvariable=username, width='40')
password_entry = Entry(textvariable=password, width='40', show='*')
fullname_entry = Entry(textvariable=fullname, width='40')
age_entry = Entry(textvariable=age, width='40')


username_entry.place(x=22, y=100)
password_entry.place(x=22, y=160)
fullname_entry.place(x=22, y=220)
age_entry.place(x=22, y=280)

submit_btn = Button(mywindow, text='Ingresar Informacion', command=send_data, width='30', height='2', bg='#00CD63')
submit_btn.place(x=22, y=320)





mywindow.mainloop()