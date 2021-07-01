import webbrowser
import tkinter
from tkinter import *

def open_instagram():
    webbrowser.open_new("")

root  = Tk()

openLABEL = Label(root,text="Lame Instagram",fg="blue")
openLABEL.grid()

openBTN = Button(root,text="Open Instagram",width = 20,command = open_instagram,font = ("jost",15))
openBTN.grid()

root.mainloop()
