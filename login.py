from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
import os
import hashlib

def mensagem_alerta(a, b):
    messagebox.showinfo(title=a, message=b)

def janela_login():
    janela_login = Tk()
    janela_login.geometry('410x450')
    janela_login.configure(background='powder blue')

    # Inserindo logo:
    pastaApp = os.path.dirname(__file__)
    imagem_logo = PhotoImage(file=pastaApp + '\\tv.png')
    imagem_logo = imagem_logo.subsample(5, 5)
    imagem = Label(janela_login, image=imagem_logo, background='powder blue')
    imagem.place(x=105, y=0)

    # Definindo as escritas:
    janela_login.title('Sistema de Empréstimo de Ferramenta')
    frase = Label(master=janela_login, text='Seja bem-vindo!', background='powder blue', font=('arial', 18))
    frase.place(x=120, y=200)

    frase = Label(master=janela_login, text='Realize o login:', background='powder blue', font=('arial', 16))
    frase.place(x=140, y=230)

    usuario = Label(master=janela_login, text='Usuário:', background='powder blue', font=('arial', 12))
    usuario.place(x=100, y=270)

    senh_a = Label(master=janela_login, text='Senha:', background='powder blue', font=('arial', 12))
    senh_a.place(x=100, y=310)

    # definindo caixas de entrada:
    nome = Entry(master=janela_login, background='powder blue')
    nome.place(x=170, y=270)

    senha = Entry(master=janela_login, background='powder blue', show="*")
    senha.place(x=170, y=310)



    # botão:
    def fun_botao1():
        if nome.get() != '':
            if senha.get() != '':
                string = senha.get().encode()
                hash = hashlib.md5(string)
                conexao = sqlite3.connect('banco_scf.db')
                c = conexao.cursor()
                c.execute(''' SELECT count(1) FROM tecnico WHERE login=:nome AND senha=:senha ''',
                          {
                              'nome': nome.get(),
                              'senha': hash.hexdigest()
                          }
                          )
                count = list(c)[0]
                conexao.commit()
                conexao.close()
                if count[0]==1:
                    mensagem_alerta('Sucesso!', 'Login realizado com sucesso')
                    janela_login.destroy()
                    os.system("python controle.py")
                else:
                    mensagem_alerta('Erro', 'Usuário ou Senha incorreto!')
            else:
                mensagem_alerta('Erro', 'Senha incorreta!')
        else:
            mensagem_alerta('Erro!', 'Usuário incorreto!')

    botao = Button(master=janela_login, text='Entrar', command=fun_botao1)
    botao.place(x=190, y=370)
    janela_login.mainloop()

if __name__=="__main__":
    janela_login()

