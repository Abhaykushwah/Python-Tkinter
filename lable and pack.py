from tkinter import *
root = Tk()
root.geometry("600x400")
root.title("Label and Pack function's")

## Important Label option 

# text - adds the text 
# bd, background - adds background
# fg, foreground - adds foreground
    ## bg='cyan' ,fg="red"

# font - set the font
    # 1. font=( "comicsansms", 25, "bold")
    # 2. font= "comicsansms" 25 "bold"

# padx - x padding 
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='''def clock(): 
        date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')
        if int(hour) > 12 and int(hour) < 24:
                time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
        else:
                time = time2 + ' ' + time3
        time_label.config(text = time)
        date_label.config(text= date)
        time_label.after(1000, clock)''',bg='cyan' ,fg="red", padx=100,pady=70, font=( "comicsansms", 25, "bold"), borderwidth=15)


title_label.pack()

root.mainloop()