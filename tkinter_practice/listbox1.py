from tkinter import *

root = Tk()

lb = Listbox(root, height=4)
lb.pack()

# ListBox 안에는 하나하나 insert 해줘야 함
lb.insert(END, "Python")
lb.insert(END, "C")
lb.insert(END, "Java")
lb.insert(END, "Swift")

root.mainloop()