# Comando abaixo importa tudo que há na bibloteca que é necessaria para a 
# criacao de telas usando tkinters ('Asterisco'*' = TUDO)
from tkinter import *

# i (instanciar) recebe o objeto tk
i = Tk()

# gerar titulo da janela
i.title("Programa financeiro")

# propriedade que altera o tamanho da janela (980x720) e distancia da direita e topo da tela (250X30)
i.geometry("980x720+250+30")

# propriedades graficas, cor de fundo da tela (bg) ou (background)
# NAO PODE PASSAR O 'i' COM PONTO! DEVE SER 'i' COM '[]'
i["bg"] = "yellow"

# CRIA ICONE NA JANELA, VOCE DEVE TER A IMAGEM NO MESMO LOCAL DO CODIGO
# i.wm_iconbitmap("icone.ico")

# cria um label e posiciona (place). ele em relacao a tela
lb = Label(i, text = "Nome do usuario")
lb.place(x = 100, y = 100)

# cria um botao e posiciona (place) ele em relacao a label
bt = Button(i, width = "20", text = "ok")
bt.place(x = 230, y = 100)

# gera a janela grafica
i.mainloop()