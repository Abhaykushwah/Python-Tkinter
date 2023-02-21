from tkinter import *
root = Tk()
root.geometry("650x400")

user = Label(text='User name')
password = Label(text='Password')
user.grid()
password.grid(row=1)

# Variable classes in tkinter 
# BooleanVar, StringVar, DoubleVar, IntVars


root.mainloop()