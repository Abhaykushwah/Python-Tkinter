from tkinter import * 
root=Tk()
root.title("Calculator")
root.geometry("415x600")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, padx=10,pady=10)
f = Frame(root, bg="gray").pack()
b = Button(f,text="9",padx=10,font="lucida 35 bold").pack()



root.mainloop()