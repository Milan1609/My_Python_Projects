from tkinter import *
from tkinter import ttk

# graphic desigen
root = Tk()

root.title('My Translator')  # title of the graphic
root.geometry('500x700')   # graphic desigen
root.config(bg='Red')  #background color

lab_text = Label(root, text = 'Translator', font = ("Time New Roman ",40,'Bold'))
lab_text.place()

root.mainloop()