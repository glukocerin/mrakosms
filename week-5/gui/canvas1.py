from tkinter import *

master = Tk()

w = Canvas(master, width=1000, height=1000)
w.pack()

step = 20
maximum = 800
for i in range(0, maximum, step):
    n = maximum - i
    w.create_line(i,0,0,n, fill="red", width=1)

mainloop()
