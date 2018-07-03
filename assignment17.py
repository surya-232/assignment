#question1
#Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.
import tkinter
from tkinter import *
import sys


root = Tk()
root.title("first_question")
root.geometry("300x100")
root.resizable(False,False)

l1=Label(root,text="hello world",width=20,bg='black',fg='white')
l1.pack()
b=Button(root, text="Exit", command=quit)
b.pack()



root.mainloop()


#question2
# Write a python program to in the same interface as above and create a action when the button is click it will display some text.
import tkinter
from tkinter import *
import sys
def show():
    l1 = Label(root, text="hello world", width=20, bg='black', fg='white')
    l1.pack()



root = Tk()
root.title("second_question")
root.geometry("300x100")
root.resizable(False,False)


b=Button(root, text="press", command=show, bg="blue")
b.pack()
b1=Button(root, text="Exit", command=quit, bg="red")
b1.pack()


root.mainloop()

#question3
#Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

import tkinter
from tkinter import *
import sys


root = Tk()
root.title("first_question")
root.geometry("500x400+5+5")
root.resizable(False,False)

l1=Label(root,text="and the text",width=20,bg='black',fg='white')
def press():
    l1.config(text="changed")
l1.pack()
b=Button(root, text="change text", command=press)
b.pack()
b1=Button(root, text="Exit", command=quit)
b1.pack()



root.mainloop()



#question4
#Write a python program using tkinter interface to take an input in the GUI program and print it.
from tkinter import *
def show():
    l3.configure(text=e1.get())
    l4.configure(text=e2.get())
root = Tk()
l1=Label(root, text="First Name").grid(row=0)
l2=Label(root, text="Last Name").grid(row=1)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
Button(root, text='Show', command=show).grid(row=3, )
l3=Label(root, text="", bg="black", fg='white')
l4=Label(root, text="", bg="white", fg="black")
l3.grid()
l4.grid()
root.title("fourth_question")
root.geometry("500x500")
root.mainloop()


