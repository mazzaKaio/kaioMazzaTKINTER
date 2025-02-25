from tkinter import *

def bt_click_soma():
    # Codigo abaixo é para validar a entrada apenas de numeros
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        resultado["text"] = num1 + num2
        resultado["bg"] = "#00FA9A"
    else:
        resultado["text"] = "valores sao invalidos"
        resultado["bg"] = "red"
    
def bt_click_sub():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        resultado["text"] = num1 - num2
        resultado["bg"] = "#00FA9A"
    else:
        resultado["text"] = "valores sao invalidos"
        resultado["bg"] = "red"

def bt_click_mult():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        resultado["text"] = num1 * num2
        resultado["bg"] = "#00FA9A"
    else:
        resultado["text"] = "valores sao invalidos"
        resultado["bg"] = "red"

def bt_click_div():
    if (str(ed1.get()).isnumeric() and str(ed2.get()).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        resultado["text"] = num1 / num2
        resultado["bg"] = "#00FA9A"
    else:
        resultado["text"] = "valores sao invalidos"
        resultado["bg"] = "red"

i = Tk()

i.title("Programa financeiro")
i.geometry("980x720+250+30")
i["bg"] = "blue"

resultado = Label(i, text = "0")
resultado.place(x="380", y="170")

bt_soma = Button(i, width="8", text="+", command=bt_click_soma)
bt_soma.place(x="260", y="210")

bt_sub = Button(i, width="8", text="-", command=bt_click_sub)
bt_sub.place(x="260", y="240")

bt_mult = Button(i, width="8", text="*", command=bt_click_mult)
bt_mult.place(x="260", y="270")

bt_div = Button(i, width="8", text="/", command=bt_click_div)
bt_div.place(x="260", y="300")

ed1 = Entry(i)
ed1.place(x="230", y="150")

ed2 = Entry(i)
ed2.place(x="230", y="180")

meuNome = Label(i, text = "Kaio Gomes do Nascimento Mazza", font = "Arial")
meuNome.place(x="200", y="350")


i.mainloop()