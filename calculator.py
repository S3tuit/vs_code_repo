from tkinter import*

#functions: add, minus, times, divide
#GUI func: write num, del num, submit

class Num_button(Button):

    def __init__ (self, num, row_n, col_n):
        super().__init__(window,
                         bg="silver",
                         fg="black",
                         text=num)
        self.grid(row=row_n,
                  column=col_n,
                  sticky="ew")

def label_top_f():

    label_top = Label(window,
                      text="0",
                      bg="black",
                      fg="#00ff00",
                      pady=13,
                      font=("Arial", 27, "bold"))
    label_top.grid(row=0, column=0, sticky="ew", columnspan=5)

window = Tk()
window.geometry("500x700")

window.grid_columnconfigure(0, weight=10)
window.grid_columnconfigure(1, weight=10)
window.grid_columnconfigure(2, weight=10)
window.grid_columnconfigure(3, weight=1)
window.grid_columnconfigure(4, weight=10)

label_top_f()
num1 = Num_button("1", 1, 0)
num2 = Num_button("2", 1, 1)
num3 = Num_button("3", 1, 2)
num4 = Num_button("4", 2, 0)
num5 = Num_button("5", 2, 1)
num6 = Num_button("6", 2, 2)
num7 = Num_button("7", 3, 0)
num8 = Num_button("8", 3, 1)
num9 = Num_button("9", 3, 2)
num_plus = Num_button("+", 1, 4)

window.mainloop()