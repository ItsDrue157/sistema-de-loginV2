from tkinter import *
import tkinter as tk
import csv

janela = tk.Tk()
janela.configure(background='purple')
janela.title("Sistema de login")
janela.geometry("500x500")

def sistema_de_login():
    janela.withdraw()  # esconde a janela antiga
    janela_de_login = tk.Toplevel(janela)
    janela_de_login.configure(background='purple')
    janela_de_login.title("Sistema de login")
    janela_de_login.geometry("500x500")

    # campo de usuario
    usuario_label = tk.Label(janela_de_login, text="Digite seu usuario: ", font=('Helvetica', 12))
    usuario_label.grid(column=0, row=0)

    usuario_entry = tk.Entry(janela_de_login, width=20)
    usuario_entry.grid(column=1, row=0)

    # campo de senha
    senha_label = tk.Label(janela_de_login, text="Digite sua senha: ", font=('Helvetica', 12))
    senha_label.grid(column=0, row=1)

    senha_entry = tk.Entry(janela_de_login, width=20, show="*")  # usando show="*" para esconder a senha
    senha_entry.grid(column=1, row=1)

    def Salvar():
        usuario = usuario_entry.get()
        senha = senha_entry.get()
        with open('meu_banco.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([usuario, senha])
        usuario_entry.delete(0, tk.END)
        senha_entry.delete(0, tk.END)

    botao_pegar_dados = Button(janela_de_login, text='cadastrar', font=('Helvetica', 12), command=Salvar)
    botao_pegar_dados.grid(column=1, row=2)

    janela_de_login.mainloop()

def App():
    botao = Button(janela, text='Bem Vindo', font=('Helvetica', 20), width=10, height=1, command=sistema_de_login)
    botao.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

App()
janela.mainloop()