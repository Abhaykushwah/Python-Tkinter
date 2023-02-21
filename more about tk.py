from tkinter import *

root=Tk()
root.geometry("644x444")  
root.title("More about Tkinter")

# adding ico
# root.wm_iconbitmap("1.ico")
root.configure(bg="light gray")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")

Button(text="Close", command=root.destroy).pack()

root.mainloop()