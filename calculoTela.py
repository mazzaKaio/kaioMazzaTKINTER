from tkinter import *

def bt_click():
    num1 = int(ed1.get())
    num2 = int(ed2.get())
    lb["text"] = num1 + num2

i = Tk()

i.title("Programa financeiro")
i.geometry("980x720+250+30")
i["bg"] = "blue"

lb = Label(i, text = "0")
lb.place(x="230", y="260")

bt = Button(i, width="20", text="Calcular", command=bt_click)
bt.place(x="230", y="230")

ed1 = Entry(i)
ed1.place(x="230", y="150")

ed2 = Entry(i)
ed2.place(x="230", y="180")

i.mainloop()