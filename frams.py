from tkinter import * 

root= Tk()
root.geometry("644x344")
root.minsize(444,244)
root.maxsize(844,444)

f1= Frame(root,bg="yellow", borderwidth=3)
f1.pack(side="left",fill="y")
l1 = Label(f1, text="Project Tkinter - Text Editor")
l1.pack()
root.mainloop()