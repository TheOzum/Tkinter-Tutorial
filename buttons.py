from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a Button!!")
    myLabel.pack()

myButton = Button(root, text="Click Me!", padx=50, pady=50, fg="blue", bg="red", command=myClick)
myButton.pack()

root.mainloop()