from tkinter import *

master = Tk()

w = Canvas(master, width=400, height=300)
w.pack()

# w.create_rectangle(50, 20, 150, 80, fill="#ff0000")
# w.create_line(0, 0 , 50, 20, fill="#00ff00", width=3)


size = 20
for i in range(64)
    x = i % 8
    y = i // 8:
    if (x+y) % 2 == 0:
        color = "#000000"
    else:
        color = "#ffffff"

    w.create_rectangle(x*size,y*size,(x+1)*size,(y+1)*size, fill=color)


#
# w.create_rectangle(0, 0, 20, 20, fill="#ff0000")
# w.create_rectangle(20, 20, 40, 40, fill="#ff0000")
# w.create_rectangle(40, 0, 60, 20, fill="#ff0000")
# w.create_rectangle(60, 20, 80, 40, fill="#ff0000")
# w.create_rectangle(80, 0, 100, 20, fill="#ff0000")
# w.create_rectangle(100, 20, 120, 40, fill="#ff0000")
# w.create_rectangle(120, 0, 140, 20, fill="#ff0000")
# w.create_rectangle(140, 20, 160, 40, fill="#ff0000")
#
# w.create_rectangle(0, 40, 20, 60, fill="#ff0000")
# w.create_rectangle(20, 60, 40, 80, fill="#ff0000")
# w.create_rectangle(40, 40, 60, 60, fill="#ff0000")
# w.create_rectangle(60, 60, 80, 80, fill="#ff0000")
# w.create_rectangle(80, 40, 100, 60, fill="#ff0000")
# w.create_rectangle(100, 60, 120, 80, fill="#ff0000")
# w.create_rectangle(120, 40, 140, 60, fill="#ff0000")
# w.create_rectangle(140, 60, 160, 80, fill="#ff0000")


mainloop()
