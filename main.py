from tkinter import *
import tkinter as tk
import sqlite3

def criar_banco_de_dados():
    global conn
    global cursor
    conn = sqlite3.connect('sistema_de_login.sql')  # vai criar ou abrir se exitir com o nome
    cursor = conn.cursor()
    print("Banco de dados conectado")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """)
    conn.commit()
    print("Tabela criada")

# Inicializar o banco de dados e criar a tabela de usu�rios
criar_banco_de_dados()

#config da gui
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

    #salvar usuario para ser depois inserido no banco de dados
    def salvar_usuario():
        usuario = usuario_entry.get()
        senha = senha_entry.get()
        inserir_usuario(usuario, senha)
        usuario_entry.delete(0, tk.END)
        senha_entry.delete(0, tk.END)
        print("Usuario cadastrado com sucesso")
    #inserir na tabela os dados gerados
    
    def inserir_usuario(usuario, senha):
        cursor.execute("INSERT INTO Users (user, password) VALUES (?, ?)", (usuario, senha))
        conn.commit()
        print("Dados inseridos")


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

    botao_sair = Button(janela_de_login, text="sair", command=janela_de_login.destroy)
    botao_sair.grid(column=3, row=5)

    botao_cadastrar = Button(janela_de_login, text='Cadastrar', font=('Helvetica', 12), command=salvar_usuario)
    botao_cadastrar.grid(column=1, row=2)
    

    janela_de_login.mainloop()

def App():
    botao = Button(janela, text='Bem Vindo', font=('Helvetica', 20), width=10, height=1, command=sistema_de_login)
    botao.place(relx=0.5, rely=0.5, anchor=tk.CENTER)



App()
janela.mainloop()