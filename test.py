import tkinter as tk
import random as rm
import time as tm

def move_circles(circle, canvas):
    global running

    if running:
        canvas.move(circle, 0, 1)
        canvas.update()
        rm_circle_crd = canvas.coords(rm_circle)
        if 185**2 >= (rm_circle_crd[0] - 185)**2 + (rm_circle_crd[1] - 185)**2:
            canvas.itemconfig(rm_circle, state="normal")
        else:
            canvas.itemconfig(rm_circle, state="hidden")
        canvas.after(10, move_circles, circle, canvas)



running = True

window = tk.Tk()

canvas = tk.Canvas(window,
                   height=370,
                   width=370,
                   bg="black")
canvas.pack()



rm_circle = canvas.create_oval(40, 40, 53, 53,
                                   fill="white",
                                   state="hidden")


square = canvas.create_rectangle(0,0,370,370,
                                 fill="silver")

circle = canvas.create_oval(0, 0, 370, 370,
                            outline="white",
                            width=3)
canvas.itemconfig(square, stipple="gray75")


window.mainloop()