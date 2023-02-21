# importing required modules 
from tkinter import *
import datetime
import time
import os
from playsound import playsound

def alarm():
    #creating alarm
    pass

def worldclock():
    # creating worldclock
    pass

def stopwatch():
    # creating stopwatch
    pass

def timer():
    # creating timer
    # playsound('sounds/timer.mp3')
    pass


# defining geometry
alarm_root = Tk()
alarm_root.geometry("650x400")
alarm_root.maxsize(650,400)
alarm_root.minsize(650,400)

# basic body
alarm_root.title("Clock")
inner_title = Label(text="Clock Application",borderwidth=6,relief="groove")
inner_title.pack(anchor="center",fill="x")

# Frame
nev_bar_frame = Frame(alarm_root, borderwidth=3) 
nev_bar_frame.pack(anchor="nw")



# Nev Buttons
nev_bar_alarm = Button(nev_bar_frame,text="Alarm", command=alarm)
nev_bar_alarm.pack(side="left")

nev_bar_WorldClock = Button(nev_bar_frame, text="World Clock", command=worldclock)
nev_bar_WorldClock.pack(side="left")

nev_bar_Stopwatch = Button(nev_bar_frame,text="StopWatch", command=stopwatch)
nev_bar_Stopwatch.pack(side="left")

nev_bar_Timer = Button(nev_bar_frame, text="Timer", command=timer)
nev_bar_Timer.pack(side="left")


# calling main loop
alarm_root.mainloop()