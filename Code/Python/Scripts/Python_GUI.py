import random
from Tkinter import *

def Number():
    label2 = label(root,text="test")
    label2.pack()
def printSomething():
    # if you want the button to disappear:
    # button.destroy() or button.pack_forget()
    label1 = Label(root, text= "Hey whatsup bro, i am doing something very interresting.")
    #this creates a new label to the GUI
    label1.pack() 

root = Tk()

button = Button(root, text="Button 1", command=printSomething) 
button.pack()

button2 = Button(root,text='Button 2',command=Number)
button2.pack()
root.mainloop()