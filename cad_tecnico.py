#-----------------------------------------------------------------------------------------------------------------------
# Classes Técnico
#-----------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import hashlib
import crud_tecnico

class TecnicoBD:
    def __init__(self, win):
        self.objBD = crud_tecnico.AppBD()

        # Inserindo Logo:
        self.image = Image.open('tecnico.png').resize((70,70))
        self.photo = ImageTk.PhotoImage(self.image)
        self.labelImage = Label(win, image=self.photo)
        self.labelImage.image = self.photo
        self.labelImage.grid(row=0, column=0, columnspan=8, padx=10, pady=20)
        self.frase = Label(win, text='Nesta tela você pode cadastrar, excluir ou atualizar técnicos.',
                           font=('arial', 12)).grid(row=1, column=0, columnspan=8, padx=10, pady=10)

        # Componente Label e Entrada de Dados
        self.lblCodigo = Label(win, text='Código').grid(row=3, column=0, padx=5, pady=5)
        self.txtCodigo = Entry(win)
        self.txtCodigo.grid(row=3, column=1, padx=5, pady=5)

        self.lblNome = Label(win, text='Nome').grid(row=3, column=2, padx=5, pady=5)
        self.txtNome = Entry(win)
        self.txtNome.grid(row=3, column=3, padx=5, pady=5)

        self.lblCpf = Label(win, text='CPF').grid(row=3, column=4, padx=5, pady=5)
        self.txtCpf = Entry(win)
        self.txtCpf.grid(row=3, column=5, padx=5, pady=5)

        self.lblCelular = Label(win, text='Celular').grid(row=3, column=6, padx=5, pady=5)
        self.txtCelular = Entry(win)
        self.txtCelular.grid(row=3, column=7, padx=5, pady=5)

        self.lblTurno = Label(win, text='Turno').grid(row=4, column=0, padx=5, pady=5)
        self.txtTurno = Entry(win)
        self.txtTurno.grid(row=4, column=1, padx=5, pady=5)

        self.lblEquipe = Label(win, text='Equipe').grid(row=4, column=2, padx=5, pady=5)
        self.txtEquipe = Entry(win)
        self.txtEquipe.grid(row=4, column=3, padx=5, pady=5)

        self.lblTipo = Label(win, text='Tipo de Usuário').grid(row=4, column=4, padx=5, pady=5)
        self.txtTipo = Entry(win)
        self.txtTipo.grid(row=4, column=5, padx=5, pady=5)

        self.lblLogin = Label(win, text='Login').grid(row=4, column=6, padx=5, pady=5)
        self.txtLogin = Entry(win)
        self.txtLogin.grid(row=4, column=7, padx=5, pady=5)

        self.lblSenha = Label(win, text='Senha').grid(row=5, column=0, padx=5, pady=5)
        self.txtSenha = Entry(win, show="*")
        self.txtSenha.grid(row=5, column=1, padx=5, pady=5)

        # Botões
        self.btnCadastrar = Button(win, text='Cadastrar', command=self.fCadastrarTecnico).grid(row=6, column=2, padx=5, pady=20)
        self.btnAtualizar = Button(win, text='Atualizar', command=self.fAtualizarTecnico).grid(row=6, column=3, padx=5, pady=20)
        self.btnExcluir = Button(win, text='Excluir', command=self.fExcluirTecnico).grid(row=6, column=4, padx=5, pady=20)
        self.btnLimpar = Button(win, text='Limpar', command=self.fLimparTela).grid(row=6, column=5, padx=5, pady=20)

        # Componentes TreeView
        self.dadosColunas = ("Codigo","Nome", "CPF", 'Celular', 'Turno', 'Equipe', 'Tipo', 'Login', 'Senha')
        self.treeTecnicos = ttk.Treeview(win, columns=self.dadosColunas, show='headings')
        self.scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=self.treeTecnicos.yview())
        self.treeTecnicos.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=7, column=9, sticky='ns', padx=5, pady=5)

        self.treeTecnicos.heading("Codigo", text="Codigo")
        self.treeTecnicos.heading("Nome", text="Nome")
        self.treeTecnicos.heading("CPF", text="CPF")
        self.treeTecnicos.heading("Celular", text="Celular")
        self.treeTecnicos.heading("Turno", text="Turno")
        self.treeTecnicos.heading("Equipe", text="Equipe")
        self.treeTecnicos.heading("Tipo", text="Tipo")
        self.treeTecnicos.heading("Login", text="Login")
        self.treeTecnicos.heading("Senha", text="Senha")

        self.treeTecnicos.column("Codigo", minwidth=0, width=50)
        self.treeTecnicos.column("Nome", minwidth=0, width=120)
        self.treeTecnicos.column("CPF", minwidth=0, width=100)
        self.treeTecnicos.column("Celular", minwidth=0, width=100)
        self.treeTecnicos.column("Turno", minwidth=0, width=100)
        self.treeTecnicos.column("Equipe", minwidth=0, width=100)
        self.treeTecnicos.column("Tipo", minwidth=0, width=100)
        self.treeTecnicos.column("Login", minwidth=0, width=100)
        self.treeTecnicos.column("Senha", minwidth=0, width=100)

        self.treeTecnicos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)
        self.treeTecnicos.grid(row=7, column=0, columnspan=9, padx=5, pady=5)

        self.carregarDadosIniciais()
# ----------------------------------------------------------------------------------------------------------------------
# Método Apresentar Registro Selecionado
# ----------------------------------------------------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeTecnicos.selection():
            item = self.treeTecnicos.item(selection)
            codigo, nome, cpf, celular, turno, equipe, tipo_user, login, senha = item["values"][0:9]
            self.txtCodigo.insert(0, codigo)
            self.txtNome.insert(0, nome)
            self.txtCpf.insert(0, cpf)
            self.txtCelular.insert(0, celular)
            self.txtTurno.insert(0, turno)
            self.txtEquipe.insert(0, equipe)
            self.txtTipo.insert(0, tipo_user)
            self.txtLogin.insert(0, login)
            self.txtSenha.insert(0, senha)
# ----------------------------------------------------------------------------------------------------------------------
# Método Carregar Dados Iniciais
# ----------------------------------------------------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objBD.selecionarDados()
            for item in registros:
                codigo = item[0]
                nome = item[1]
                cpf = item[2]
                celular = item[3]
                turno = item[4]
                equipe = item[5]
                tipo_user = item[6]
                login = item[7]
                senha = item[8]
                self.treeTecnicos.insert('', 'end', iid=self.iid, values=(codigo, nome, cpf, celular, turno, equipe,
                                                                          tipo_user, login, senha))
                self.iid = self.iid + 1
                self.id = self.id + 1
        except:
            print("Ainda não existem dados para carregar")

# ----------------------------------------------------------------------------------------------------------------------
# Método Ler Dados da Tela
# ----------------------------------------------------------------------------------------------------------------------
    def fLerCampos(self):
        try:
            codigo = int(self.txtCodigo.get())
            nome = self.txtNome.get()
            cpf = self.txtCpf.get()
            celular = self.txtCelular.get()
            turno = self.txtTurno.get()
            equipe = self.txtEquipe.get()
            tipo_user = self.txtTipo.get()
            login = self.txtLogin.get()
            senha = self.txtSenha.get()
        except:
            print("Não foi possível ler os dados.")
        return codigo, nome, cpf, celular, turno, equipe, tipo_user, login, senha
#----------------------------------------------------------------------------------------------------------------------
# Método Cadastrar Produto
#----------------------------------------------------------------------------------------------------------------------
    def fCadastrarTecnico(self):
        try:
            nome = self.txtNome.get()
            cpf = self.txtCpf.get()
            celular = self.txtCelular.get()
            turno = self.txtTurno.get()
            equipe = self.txtEquipe.get()
            tipo_user = self.txtTipo.get()
            login = self.txtLogin.get()
            senha = self.txtSenha.get()
            self.string = senha.encode()
            self.hash = hashlib.md5(self.string)
            self.hash = self.hash.hexdigest()
            self.objBD.inserirDados(nome, cpf, celular, turno, equipe, tipo_user, login, self.hash)
            self.treeTecnicos.delete(*self.treeTecnicos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
        except:
            print("Não foi possível fazer o cadastro")
#----------------------------------------------------------------------------------------------------------------------
# Método Limpar Tela
#----------------------------------------------------------------------------------------------------------------------
    def fLimparTela(self):
        try:
            self.txtNome.delete(0, END)
            self.txtCpf.delete(0, END)
            self.txtCelular.delete(0, END)
            self.txtTurno.delete(0, END)
            self.txtEquipe.delete(0, END)
            self.txtTipo.delete(0, END)
            self.txtLogin.delete(0, END)
            self.txtSenha.delete(0, END)
            self.txtCodigo.delete(0, END)
        except:
            print("Não foi possível Limpar os campos")
#-----------------------------------------------------------------------------------------------------------------------
# Método Excluir Tecnico
#-----------------------------------------------------------------------------------------------------------------------
    def fExcluirTecnico(self):
        try:
            codigo, nome, cpf, celular, turno, equipe, tipo_user, login, senha = self.fLerCampos()
            self.objBD.excluirDados(codigo)
            # Recarrega dados na tela
            self.treeTecnicos.delete(*self.treeTecnicos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
        except:
            print("Não foi possível fazer a exclusão")

#-----------------------------------------------------------------------------------------------------------------------
# Método Atualizar Tecnico
#-----------------------------------------------------------------------------------------------------------------------
    def fAtualizarTecnico(self):
        try:
            codigo, nome, cpf, celular, turno, equipe, tipo_user, login, senha = self.fLerCampos()
            self.string = senha.encode()
            self.hash = hashlib.md5(self.string)
            self.hash = self.hash.hexdigest()
            self.objBD.atualizarDados(codigo, nome, cpf, celular, turno, equipe, tipo_user, login, self.hash)
            # Recarrega dados na tela
            self.treeTecnicos.delete(*self.treeTecnicos.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
        except:
            print("Não foi possível fazer a atualização")



if __name__ == "__main__":
    janela = Tk()
    janela.geometry("940x650")
    janela.title('Bem Vindo a Aplicação de Banco de Dados')
    frame_tecnico = Frame(janela, width=930, height=650)
    TecnicoBD(frame_tecnico)
    frame_tecnico.pack()
    janela.mainloop()
