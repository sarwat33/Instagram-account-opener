import webbrowser
import tkinter
from tkinter import *

def open_google():
    webbrowser.open_new("")

root  = Tk()

openLABEL = Label(root,text="Lame Google",fg="blue")
openLABEL.grid()

openBTN = Button(root,text="Open Google",width = 20,command = open_google,font = ("jost",15))
openBTN.grid()

root.mainloop()
