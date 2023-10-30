from tkinter import *
import random
import time

def label_1():

    label = Label(window,
                  text="Test Your Reflex!",
                  font=("Arial", 37, "bold"),
                  fg="white",
                  padx=23,
                  bg="black",
                  )
    label.pack()

def sub_heading():

    #global icon
    #icon = PhotoImage(file="lighting.png")

    label = Label(window,
                  text="... and then flex",
                  font=("Arial", 17, "italic"),
                  fg="silver",
                  padx=13,
                  pady=7,
                  compound="right",
                  bg="black",
                  )
    label.pack()

def bg_change():
    global start_time
    global end_time
    global count
    global mist

    chance=random.randint(0, 21)
    if chance == 1 and mist == False:
        count = 0
        label_change.config(bg="#00ff00")
        start_time = time.time()
        label_change.bind("<Button-1>", calc_ref)
    elif mist == False:
        label_change.after(100, bg_change)
    else:
        pass

def calc_ref(event):
    global start_time
    global end_time

    label_change.unbind("<Button-1>")
    start_game.config(state="active")
    end_time = time.time()
    label_change.config(bg="silver")
    print(end_time - start_time)

def mistake(event):
    global mist

    mist = True
    label_change.config(bg="red")
    start_game.config(state="active")
    print("DUUUUMB!")

def starting():
    global mist

    mist = False
    label_change.bind("<Button-1>", mistake)
    label_change.config(bg="silver")
    start_game.config(state="disabled")
    label_change.after(500, bg_change)


start_time = 0
end_time = 0
count = 0
mist = False

window = Tk()
window.geometry("570x570")
window.title("Ref-Flex")

window.config(bg="black")

label_1()
sub_heading()

start_game = Button(window,
                    text="Start the game",
                    command=starting,
                    font=("Impact", 13),
                    bg="White",
                    fg="black",
                    pady=7
)
start_game.pack()

label_change = Label(window,
                  bg="silver",
                  width=70,
                  height=17
                  )
label_change.pack()

window.mainloop()