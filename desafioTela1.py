from tkinter import *
i = Tk()

i.title("Programa financeiro")
i.geometry("980x720+250+30")

lbVazia = Label(i, text="", width=20, height=4)
lbVazia.pack(fill=X, side=TOP, anchor=E)

lbVazia = Label(i, text="", width=10)
lbVazia.pack(fill=Y, side=RIGHT)

ed1 = Entry(i, width=25)
ed1.pack(side=TOP, anchor=E)

lb1 = Label(i, text="Login", bg="lightyellow", width=21)
# componente '.grid' serve tambem para posicionar utilizando indicativo de 'row' e 'column'
lb1.pack(side=TOP, anchor=E)

lbVazia = Label(i, text="")
lbVazia.pack(fill=X, side=TOP, anchor=E)

ed2 = Entry(i, width=25)
ed2.pack(side=TOP, anchor=E)

lb2 = Label(i, text="Senha", bg="lightblue", width=21)
lb2.pack(side=TOP, anchor=E)

lbVazia = Label(i, text="")
lbVazia.pack(expand=0, anchor=CENTER)

bt1 = Button(i, text="Logar", width=15, height=2)
bt1.pack(side=TOP, anchor=CENTER, expand=1)

i.mainloop()