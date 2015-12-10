from tkinter import *

master = Tk()

w = Canvas(master, width=900, height=900)
w.pack()


w.create_line(450,0,450,900, fill="red", width=1)
w.create_line(0,300,900,600, fill="red", width=1)





mainloop()
