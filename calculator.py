from tkinter import*

#functions: add, minus, times, divide
#GUI func: write num, del num, submit

class Num_button(Button):

    def __init__ (self, num, row_n, col_n):
        super().__init__(window,
                         bg="silver",
                         fg="black",
                         text=num,
                         command=self.button_print)
        self.num = int(num)
        self.grid(row=row_n,
                  column=col_n,
                  sticky="ew")

    def button_print(self):
        global label_top

        current_text = label_top.cget("text")
        new_text = str(current_text) + str(self.num)
        label_top.config(text=new_text)

class Func_button(Button):

    def __init__ (self, sign, row_n, col_n):
        super().__init__(window,
                         bg="silver",
                         fg="black",
                         text=sign,
                         command=self.func)
        self.sign = sign
        self.grid(row=row_n,
                  column=col_n,
                  sticky="ew")
        
    def func(self):
        global label_top
        global last_func
        global current_num

        try:
            last_func = self.sign
            current_num = int(label_top.cget("text"))
            label_top.config(text="")
        except ValueError:
            pass

class Subm_button(Button):

    def __init__ (self, row_n, col_n):
        super().__init__(window,
                         bg="silver",
                         fg="black",
                         text="=",
                         command=self.subm)
        self.grid(row=row_n,
                  column=col_n,
                  sticky="ew")
        
    def subm(self):
        global label_top
        global last_func
        global current_num

        try:
            if last_func == "+":
                new_nums = int(label_top.cget("text")) + current_num
                label_top.config(text=new_nums)
                current_num = 0
                last_func = ""
            elif last_func == "-":
                new_nums = current_num - int(label_top.cget("text"))
                label_top.config(text=new_nums)
                current_num = 0
                last_func = ""
            elif last_func == "":
                pass
        except ValueError:
            pass


def label_top_f():
    global label_top
    label_top = Label(window,
                      text="",
                      bg="black",
                      fg="#00ff00",
                      pady=13,
                      font=("Arial", 27, "bold"))
    label_top.grid(row=0, column=0, sticky="ew", columnspan=5)


def button_del():
    global label_top
    current_text = label_top.cget("text")
    label_top.config(text=current_text[0:-1])

def button_ac():
    global label_top
    global current_num
    global last_func
    last_func = ""
    current_num = 0
    label_top.config(text="")

window = Tk()
window.geometry("500x700")
last_func = ""
current_num = 0

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
num0 = Num_button("0", 4, 0)
num_add = Func_button("+", 1, 4)
num_add = Func_button("-", 2, 4)
num_subm = Subm_button(3, 4)

num_del = Button(window,
                bg="silver",
                fg="black",
                text="Del",
                command=button_del
                )
num_del.grid(row=4,
            column=4,
            sticky="ew")

num_ac = Button(window,
                bg="silver",
                fg="black",
                text="AC",
                command=button_ac
                )
num_ac.grid(row=4,
            column=2,
            sticky="ew")

window.mainloop()