from tkinter import *
from functools import partial

#This is a project created using the Tkinter library

#validate function
def validate(username, password):
    print("Username: ", username.get())
    print("Password: ", password.get())
    return

#TK Window
window = Tk()
window.geometry('400x200')
window.title('Register')

# GUI Username & Entry box
Lusername = Label(window, text="Username").grid(row=0, column=0)
username = StringVar() #StringVar is used to edit widget textfields
EnteredUsername = Entry(window, textvariable=username).grid(row=0, column=1)

# GUI Password & Entry box
Lpassword = Label(window, text="Password").grid(row=1, column=0)
password = StringVar()
EnteredPassword = Entry(window, textvariable=password, show='*').grid(row=1, column=1)

#validate login
validate = partial(validate, username, password)

#login button
login = Button(window, text="Login", command=validate).grid(row=4, column=0)

#loop until the window is closed
window.mainloop()