from tkinter import *
import random

def click():
    global clicks
    clicks += 1
    text["text"] = f"Количество кликов:{clicks}"
    btn.place(x=random.randint(1,150), y=random.randint(1,170))

root =Tk()
root["bg"] = "black"
root.title("Clicker by _sineD_0")
root.resizable(width=False,height=False)

clicks = 0 

text = Label(text=f"Количество кликов:{clicks}",bg="black",fg="blue")
btn = Button(text="Click",bg="black",fg="Blue",command=click)

text.place(x=10, y=0)
btn.place(x=10, y=20)

root.mainloop()