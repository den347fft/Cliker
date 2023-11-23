from tkinter import *
import random

def click():
    global clicks,add
    clicks += add
    text["text"] = f"Количество кликов:{clicks}"
    btn.place(x=random.randint(1,150), y=random.randint(1,170))
    if clicks >= 10:
        root.resizable(width=True,height=False)
        btn.place(x=random.randint(1,500), y=random.randint(1,170))
    if clicks >= 20:
        root.resizable(width=False,height=True)
        btn.place(x=random.randint(1,150), y=random.randint(1,500))
    if clicks >= 30:
        root.resizable(width=False,height=False)
        root["bg"] = "Gray"
        btn.place(x=random.randint(1,150), y=random.randint(1,170))
    if clicks >= 40:
        btn["bg"] = "Gray"
        btn.place(x=random.randint(1,150), y=random.randint(1,170))
    if clicks >= 50:
        text["bg"] = "Gray"
        btn.place(x=random.randint(1,150), y=random.randint(1,170))
    if clicks >= 60:
        text["fg"] = "Gray"
        text["text"] = f"Удачи:) Количество кликов:{clicks}"
        btn["bg"] = "blue"
        btn["border"] = 0
        root["bg"] = "blue"
        text["bg"] = "blue"
        btn.place(x=random.randint(1,150), y=random.randint(1,170))
    if clicks >= 70:
        text["fg"] = "Blue"
        text["text"] = f"Количество кликов:{clicks}"
        btn["bg"] = "black"
        btn["border"] = 2
        root["bg"] = "black"
        text["bg"] = "black"
        btn.place(x=random.randint(1,150), y=random.randint(1,170))
        bf.place(x=random.randint(1,150), y=random.randint(1,170))
    if clicks >= 1000:
        text["fg"] = "Blue"
        text["text"] = f"Количество кликов:{clicks}"
        btn["bg"] = "black"
        btn["border"] = 2
        root["bg"] = "black"
        text["bg"] = "black"
        btn.place(x=random.randint(1,150), y=random.randint(1,170))
        bf.place(x=random.randint(1,150), y=random.randint(1,170))
def clear():
    global clicks,add
    clicks = 0
    add += 10
    bf.place(x=10000,y=10000)
root = Tk()
root["bg"] = "black"
root.title("Clicker by _sineD_0")
root.resizable(width=False,height=False)

clicks = 0 
add = 1

text = Label(text=f"Количество кликов:{clicks}",bg="black",fg="blue")
btn = Button(text="Нажми",bg="black",fg="Blue",command=click,cursor="cross")
bf = Button(text="Не трогай",bg="black",fg="Blue",command=clear,cursor="cross")
text.place(x=10, y=0)
btn.place(x=10, y=20)

root.mainloop()