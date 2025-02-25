from tkinter import *
i = Tk()

i.title("Programa financeiro")
i.geometry("980x720+250+30")

lb1 = Label(i, text="Label 1", bg="yellow", font="Arial")

lb2 = Label(i, text="Label 2", bg="pink", font="Arial")

lb3 = Label(i, text="Label 3", bg="limegreen", font="Arial")

lb4 = Label(i, text="Label 4", bg="lightblue", font="Arial")

# O codigo abaixo posiciona cada label em lugares diferentes, apos testar comente a linha do lb1 até o lb4


lb1.pack(side=LEFT)
lb2.pack(side="left")
lb3.pack(anchor="w") # sempre que nao utilizo a opcao 'side' ele sempre sera 'top'
# lb4.pack(anchor="w") # sempre que nao utilizo a opcao 'side' ele sempre sera 'top'

# lb4.pack(side=BOTTOM, anchor=SW)

lb4.pack(anchor=E)

i.mainloop()