# Importando dependencias do Tkinter
from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# Importando o pillow
import os
from PIL import ImageTk, Image

# Cores
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#e5e5e5" # Grey
co3 = "#00a095" # Verde
co4 = "#403d3d"  # Letra
co6 = "#003452"  # Azul
co7 = "#ef5350"  #Vermelha

co6 = "#038cfc"  # Azul
co8 = "#263238"  # + Verde
co9 = "#e9edf5"  # + Verde

# Criando Janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)


# Trabalhando no Frame Logo -------------------------------------------------

# Caminho absoluto para o arquivo logo.png
diretorio_atual = os.path.dirname(__file__)
caminho_logo = os.path.join(diretorio_atual, 'logo.png')

# Abrir a imagem com caminho seguro
app_lg = Image.open(caminho_logo)

#app_lg = Image.open('../logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="Cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)





janela.mainloop()



