from tkinter import *
from tkinter import ttk
from banco import inserir

janela = Tk()
janela.title("Cadastro de Filmes")
janela.geometry("400x300")

Label(janela, text="Nome do Filme").pack()

nome = Entry(janela, width=35)
nome.pack()

Label(janela, text="Gênero").pack()

genero = Entry(janela, width=35)
genero.pack()

Label(janela, text="Nota").pack()

nota = Entry(janela, width=10)
nota.pack()

Label(janela, text="Assistido").pack()

assistido = ttk.Combobox(janela, values=["Sim", "Não"], state="readonly")
assistido.current(0)
assistido.pack()

def salvar():
    inserir(
        nome.get(),
        genero.get(),
        nota.get(),
        assistido.get()
    )

    nome.delete(0, END)
    genero.delete(0, END)
    nota.delete(0, END)
    assistido.current(0)

Button(
    janela,
    text="Salvar",
    command=salvar
).pack(pady=20)

janela.mainloop()