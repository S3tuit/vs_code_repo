import tkinter as tk
import time

def move_circle():
    while True:
        canvas.move(circle,Xv,Yv)
        root.update()
        time.sleep(0.03)
        x1, y1, x2, y2 = canvas.coords(circle)
        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        move_curve(center_x, center_y, x2, y2)

def move_curve(x1, y1, x2, y2):
    global points
    root.update()
    points.append(x1)
    points.append(y1)
    points.append(x1)
    points.append(y1)
    root.update()
    circle = canvas.create_line(points, smooth = True, fill="red")


points = []

Xv=3
Yv=-3

root = tk.Tk()

canvas = tk.Canvas(root,
                   height=570,
                   width=570,
                   bg="black")
canvas.pack()

curve = canvas.create_line(290, 290,
                            300, 300,
                            smooth = True, fill="red")

circle = canvas.create_oval(290, 290,
                            300, 300,
                            fill="white")

move_circle()

root.mainloop()