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
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text="  Cadastro de Alunos", width=850, compound=LEFT, relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co6, fg=co1)
app_logo.place(x=0, y=0)

# funcção para cadastra alunos
def alunos():
    print('Aluno')



# Função para adicionar cursos e turmas
def adicionar():
    print('Cursos e turmas')


# Função para salvar
def salvar():
    print('Salvar')


# Função de Control------------------------------------------------------------------

def control(i):
    # cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a função alunos
        alunos()

    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a função adicionar
        adicionar()

    if i == 'salvar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()

        for widget in frame_tabela.winfo_children():
            widget.destroy()

        # chamando a função salvar
        salvar() 





# Criando botoes
    # Caminho absoluto para o arquivo add.png
diretorio_atual = os.path.dirname(__file__)
caminho_app_img_cadastro = os.path.join(diretorio_atual, 'add.png')

app_img_cadastro = Image.open(caminho_app_img_cadastro)
app_img_cadastro = app_img_cadastro.resize((18,18))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text=" Cadastro", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=10, y=30)

    # Caminho absoluto para o arquivo add.png
diretorio_atual = os.path.dirname(__file__)
caminho_app_img_adicionar = os.path.join(diretorio_atual, 'add.png')

app_img_adicionar = Image.open(caminho_app_img_adicionar)
app_img_adicionar = app_img_adicionar.resize((18,18))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adicionar, text=" Adicionar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.place(x=123, y=30)

    # Caminho absoluto para o arquivo add.png
diretorio_atual = os.path.dirname(__file__)
caminho_app_img_salvar = os.path.join(diretorio_atual, 'save.png')

app_img_salvar = Image.open(caminho_app_img_salvar)
app_img_salvar = app_img_salvar.resize((18,18))
app_img_salvar = ImageTk.PhotoImage(app_img_salvar)
app_salvar = Button(frame_dados, command=lambda:control('salvar'), image=app_img_salvar, text=" Salvar", width=100, compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_salvar.place(x=236, y=30)









janela.mainloop()



