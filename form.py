from tkinter import *

root = Tk()

def submit():
    print(f"{namevalue.get(), phonevalue.get(), sectionvalue.get(), gendervalue.get(), clubvalue.get(), membervalue.get()}")
    print("Form Submited")
    with open("recordes.txt","a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), sectionvalue.get(), gendervalue.get(), clubvalue.get(), membervalue.get()}")





root.geometry("500x300")
root.minsize(400,250)


# Heading
Label(root, text="Registration Form", font="comicsansms 13 bold", pady=10).grid(row=0, column=3)

# Text values for from
name = Label(root, text="Name")
phone = Label(root, text="Phone")
section = Label(root, text="Section")
gender = Label(root, text="Gender")
club = Label(root, text="Club Name")


# packing of Label using Grid
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
section.grid(row=3, column=2)
gender.grid(row=4, column=2)
club.grid(row=5, column=2)

# creating variables for form
namevalue = StringVar()
phonevalue = StringVar()
sectionvalue = StringVar()
gendervalue = StringVar()
clubvalue = StringVar()
membervalue = IntVar()


# getting entries for the from
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
sectionentry = Entry(root, textvariable=sectionvalue)
genderentry = Entry(root, textvariable=gendervalue)
clubentry = Entry(root, textvariable=clubvalue)

# packing of entries
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
sectionentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
clubentry.grid(row=5,column=3)

# checkbox
memberORnot = Checkbutton(text="Are you member of Abacus or not", command=submit, variable=membervalue)
memberORnot.grid(row=6, column=3)

# sumbi button
Button(text="Submit",command=submit).grid(row=7,column=3)

root.mainloop()