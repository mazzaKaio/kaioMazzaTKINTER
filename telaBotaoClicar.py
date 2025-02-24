from tkinter import *

# criando uma funcao para acao de clicar em um botao
def bt_click():
    # o label que usa propriedade 'text' recebera a mensagem "Trocou o texto"
    lb["text"] = "Trocou o texto"
    # o print abaixo exibe o texto na tela do console
    print("o botao foi clicado!")

def bt_clicking():
    # esse print exibe o teexto digitado na caixa de texto e exibe na label da tela
    print(ed.get())
    lb["text"] = ed.get()

# i (instanciar) recebe o objeto Tk
i = Tk()

# gerar titulo da janela
i.title("Programa financeiro")
i.geometry("980x720+250+30")
i["bg"] = "green"
# i.wm_iconbitmap("icone.ico")

lb = Label(i, text = "Nome do usuario")
lb.place(x = "100", y = "100")

bt = Button(i, width = "20", text = "ok", command = bt_click)
bt.place(x = "230", y = "100")

# o codigo abaixo cria um botao e posiciona abaixo do botton 'ok'
bt2 = Button(i, width = "20", text = "Capturar", command = bt_clicking)
bt2.place(x = "230", y = "190")

# cria a caixa de texto (textfield) para digitar algo
ed = Entry(i)
ed.place(x="230", y="150")

i.mainloop()