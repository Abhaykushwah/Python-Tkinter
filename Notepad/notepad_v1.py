from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os



# defining functions

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "</> by Abhay with Love")

root=Tk()
root.geometry("1200x500")
root.minsize(450,275)
root.title("Untitled - Notepad")
# ico = PhotoImage(file="notepad.png")
root.iconphoto(False, PhotoImage(file='notepad.png'))

# mymenu = Menu(root)
# mymenu.add_command(label="File", command=file)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)


#Add TextArea
TextArea = Text(root, font="lucida 13")
file = None
TextArea.pack(expand=True, fill=BOTH)

mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New File...",command=newFile)
m1.add_command(label="Open File...",command=openFile)
m1.add_separator()
m1.add_command(label="Save",command=saveFile)
m1.add_separator()
m1.add_command(label="Exit",command=quitApp)
mainmenu.add_cascade(label="File",menu=m1)


m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut",command=cut)
m2.add_command(label="Copy",command=copy)
m2.add_command(label="Paste",command=paste)
# m2.add_separator()
# m2.add_command(label="Find")
mainmenu.add_cascade(label="Edit",menu=m2)

# Help Menu 
HelpMenu = Menu(mainmenu, tearoff=0)
HelpMenu.add_command(label = "About Notepad", command=about)
mainmenu.add_cascade(label="Help", menu=HelpMenu)


mainmenu.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)

 #Adding Scrollbar using rules from Tkinter
Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT,  fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)
root.mainloop()