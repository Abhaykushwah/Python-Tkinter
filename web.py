from tkinter import *
import webview
  
tk = Tk()
tk.geometry("800x450")
  

webview.create_window('Portfolio', 'https://glauniversity.in')
webview.start()