from tkinter import *
i = Tk()

i.title("Programa financeiro")
i.geometry("980x720+250+30")

# O codigo abaixo faz correcao da posicao das labels
lb1 = Label(i, text="Login", bg="lightyellow", width=15)
lb1.grid(row=1, column=1)
# componente '.grid' serve tambem para posicionar utilizando indicativo de 'row' e 'column'
lb2 = Label(i, text="Senha", bg="lightblue", width=15)
lb2.grid(row=3, column=1)

ed1 = Entry(i, width=25)
ed1.grid(row=1, column=2)

ed2 = Entry(i, width=25)
ed2.grid(row=3, column=2)

bt1 = Button(i, text="Logar", width=15, height=2)
bt1.grid(row=5, column=1)

lb3 = Label(i, text="", width=5, height=3)
lb3.grid(row=0)

lb4 = Label(i, text="")
lb4.grid(row=2)

lb5 = Label(i, text="")
lb5.grid(row=4)

i.mainloop()