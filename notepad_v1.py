from tkinter import *
root=Tk()

# defining functions
def file():
    pass
    print("Hello from console")

# root.geometry("600x360")
root.title("Menu in Tkinter")


# mymenu = Menu(root)
# mymenu.add_command(label="File", command=file)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New File...",command=file)
m1.add_command(label="Open File...",command=file)
m1.add_separator()
m1.add_command(label="Save",command=file)
m1.add_command(label="Save As",command=file)
mainmenu.add_cascade(label="File",menu=m1)


m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut",command=file)
m2.add_command(label="Copy")
m2.add_command(label="Paste")
m2.add_separator()
m2.add_command(label="Find")
mainmenu.add_cascade(label="Edit",menu=m2)

mainmenu.add_command(label="Exit", command=quit)

Scrollbar=Scrollbar(root)
Scrollbar.pack(side="right", fill=Y)
text=Text(root, yscrollcommand=Scrollbar.set)
text.pack(fill=BOTH)
Scrollbar.config(command=text.yview)
root.config(menu=mainmenu)
root.mainloop()