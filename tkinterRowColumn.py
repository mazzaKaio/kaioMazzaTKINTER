from tkinter import *
i = Tk()

i.title("Programa financeiro")
i.geometry("980x720+250+30")

lb1 = Label(i, text="Login", bg="lightyellow")
# componente '.grid' serve tambem para posicionar utilizando indicativo de 'row' e 'column'
lb1.pack(side=RIGHT, anchor=N)


lb2 = Label(i, text="Senha", bg="lightblue")
lb2.pack(side=RIGHT, anchor=N)


ed1 = Entry(i)
ed1.pack(side=TOP)


ed2 = Entry(i)
ed2.pack(side=RIGHT)


bt1 = Button(i, text="Logar")
bt1.pack(side=RIGHT)

i.mainloop()