from tkinter import *
i = Tk()

i.title("Programa financeiro")
i.geometry("980x720+250+30")

lb1 = Label(i, text="Label 1", bg="yellow", font="Arial")
lb1.place(x=230, y=200)

lb2 = Label(i, text="Label 2", bg="pink", font="Arial")
lb2.place(x=230, y=200)

lb3 = Label(i, text="Label 3", bg="limegreen", font="Arial")
lb3.place(x=230, y=200)

lb4 = Label(i, text="Label 4", bg="lightblue", font="Arial")
lb4.place(x=230, y=200)

"""
lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack()
"""

# o codigo abaixo e responsavel pelo posicionamento dos labels
"""
lb1.pack(side="top")
lb2.pack(side="left")
lb3.pack(side="right")
lb4.pack(side="bottom")
"""

lb1.pack(side="left")
lb2.pack(side="left")
lb3.pack(side="top")
lb4.pack(side="top")

i.mainloop()