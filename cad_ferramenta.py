#----------------------------------------------------------------------------------------------------------------------
# Classes Ferramenta
#----------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import messagebox
import crud_ferramenta

class FerramentaBD:
    def __init__(self, win):
        self.objBD = crud_ferramenta.AppBD()

        # Inserindo Logo:
        self.image = Image.open('ferramenta.png').resize((70,70))
        self.photo = ImageTk.PhotoImage(self.image)
        self.labelImage = Label(win, image=self.photo)
        self.labelImage.image = self.photo
        self.labelImage.grid(row=0, column=0, columnspan=8, padx=10, pady=20)
        self.frase = Label(win, text='Nesta tela você pode cadastrar, excluir ou atualizar ferramentas.',
                           font=('arial', 12)).grid(row=1, column=0, columnspan=8, padx=10, pady=10)

        # Componente Label e Entrada de Dados
        self.lblCodigo = Label(win, text='Código').grid(row=3, column=0, padx=5, pady=5)
        self.txtCodigo = Entry(win)
        self.txtCodigo.grid(row=3, column=1, padx=5, pady=5)

        self.lblDescricao = Label(win, text='Descrição').grid(row=3, column=2, padx=5, pady=5)
        self.txtDescricao = Entry(win)
        self.txtDescricao.grid(row=3, column=3, padx=5, pady=5)

        self.lblFabricante = Label(win, text='Fabricante').grid(row=3, column=4, padx=5, pady=5)
        self.txtFabricante = Entry(win)
        self.txtFabricante.grid(row=3, column=5, padx=5, pady=5)

        self.lblVoltagem = Label(win, text='Voltagem').grid(row=3, column=6, padx=5, pady=5)
        self.txtVoltagem = Entry(win)
        self.txtVoltagem.grid(row=3, column=7, padx=5, pady=5)

        self.lblSerial = Label(win, text='N. Serial').grid(row=4, column=0, padx=5, pady=5)
        self.txtSerial = Entry(win)
        self.txtSerial.grid(row=4, column=1, padx=5, pady=5)

        self.lblTamanho = Label(win, text='Tamanho').grid(row=4, column=2, padx=5, pady=5)
        self.txtTamanho = Entry(win)
        self.txtTamanho.grid(row=4, column=3, padx=5, pady=5)

        self.lblTipo = Label(win, text='Tipo Ferramenta').grid(row=4, column=4, padx=5, pady=5)
        self.txtTipo = Entry(win)
        self.txtTipo.grid(row=4, column=5, padx=5, pady=5)

        self.lblTempo = Label(win, text='Tempo de Reserva').grid(row=4, column=6, padx=5, pady=5)
        self.txtTempo = Entry(win)
        self.txtTempo.grid(row=4, column=7, padx=5, pady=5)

        # Botões
        self.btnCadastrar = Button(win, text='Cadastrar', command=self.fCadastrarFerramenta).grid(row=5, column=2, padx=5, pady=20)
        self.btnAtualizar = Button(win, text='Atualizar', command=self.fAtualizarFerramenta).grid(row=5, column=3, padx=5, pady=20)
        self.btnExcluir = Button(win, text='Excluir', command=self.fExcluirFerramenta).grid(row=5, column=4, padx=5, pady=20)
        self.btnGExcel = Button(win, text='Gerar Excel', command=self.fGerarExcel).grid(row=5, column=5, padx=5, pady=20)
        self.btnLimpar = Button(win, text='Limpar', command=self.fLimparTela).grid(row=5, column=6, padx=5, pady=20)

        # Componentes TreeView
        self.dadosColunas = ("Codigo", "Descricao", "Fabricante", 'Voltagem', 'Serial', 'Tamanho', 'Tipo', 'Tempo')
        self.treeFerramenta = ttk.Treeview(win, columns=self.dadosColunas, show='headings')
        self.scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=self.treeFerramenta.yview())
        self.treeFerramenta.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=6, column=8, sticky='ns', padx=5, pady=5)

        self.treeFerramenta.heading("Codigo", text="Codigo")
        self.treeFerramenta.heading("Descricao", text="Descricao")
        self.treeFerramenta.heading("Fabricante", text="Fabricante")
        self.treeFerramenta.heading("Voltagem", text="Voltagem")
        self.treeFerramenta.heading("Serial", text="Serial")
        self.treeFerramenta.heading("Tamanho", text="Tamanho")
        self.treeFerramenta.heading("Tipo", text="Tipo")
        self.treeFerramenta.heading("Tempo", text="Tempo")


        self.treeFerramenta.column("Codigo", minwidth=0, width=50)
        self.treeFerramenta.column("Descricao", minwidth=0, width=150)
        self.treeFerramenta.column("Fabricante", minwidth=0, width=120)
        self.treeFerramenta.column("Voltagem", minwidth=0, width=100)
        self.treeFerramenta.column("Serial", minwidth=0, width=100)
        self.treeFerramenta.column("Tamanho", minwidth=0, width=100)
        self.treeFerramenta.column("Tipo", minwidth=0, width=120)
        self.treeFerramenta.column("Tempo", minwidth=0, width=100)

        self.treeFerramenta.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)
        self.treeFerramenta.grid(row=6, column=0, columnspan=8, padx=5, pady=5)

        self.carregarDadosIniciais()
# ----------------------------------------------------------------------------------------------------------------------
# Método Apresentar Registro Selecionado
# ----------------------------------------------------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeFerramenta.selection():
            item = self.treeFerramenta.item(selection)
            codigo, descricao, fabricante, voltagem, serial, tamanho, tipo, tempo = item["values"][0:8]
            self.txtCodigo.insert(0, codigo)
            self.txtDescricao.insert(0, descricao)
            self.txtFabricante.insert(0, fabricante)
            self.txtVoltagem.insert(0, voltagem)
            self.txtSerial.insert(0, serial)
            self.txtTamanho.insert(0, tamanho)
            self.txtTipo.insert(0, tipo)
            self.txtTempo.insert(0, tempo)
# ----------------------------------------------------------------------------------------------------------------------
# Método Carregar Dados Iniciais
# ----------------------------------------------------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
            self.iid = 0
            self.registros = self.objBD.selecionarDados()
            for item in self.registros:
                codigo = item[0]
                descricao = item[1]
                fabricante = item[2]
                voltagem = item[3]
                serial = item[4]
                tamanho = item[5]
                tipo = item[6]
                tempo = item[7]
                self.treeFerramenta.insert('', 'end', iid=self.iid, values=(codigo, descricao, fabricante, voltagem,
                                                                          serial, tamanho, tipo, tempo))
                self.iid = self.iid + 1
        except:
            print("Ainda não existem dados para carregar")
# ----------------------------------------------------------------------------------------------------------------------
# Método Ler Dados da Tela
# ----------------------------------------------------------------------------------------------------------------------
    def fLerCampos(self):
        try:
            codigo = int(self.txtCodigo.get())
            descricao = self.txtDescricao.get()
            fabricante = self.txtFabricante.get()
            voltagem = self.txtVoltagem.get()
            serial = self.txtSerial.get()
            tamanho = self.txtTamanho.get()
            tipo = self.txtTipo.get()
            tempo = self.txtTempo.get()
        except:
            print("Não foi possível ler os dados.")
        return codigo, descricao, fabricante, voltagem, serial, tamanho, tipo, tempo
#----------------------------------------------------------------------------------------------------------------------
# Método Cadastrar Ferramenta
#----------------------------------------------------------------------------------------------------------------------
    def fCadastrarFerramenta(self):
        try:
            descricao = self.txtDescricao.get()
            fabricante = self.txtFabricante.get()
            voltagem = self.txtVoltagem.get()
            serial = self.txtSerial.get()
            tamanho = self.txtTamanho.get()
            tipo = self.txtTipo.get()
            tempo = self.txtTempo.get()
            self.objBD.inserirDados(descricao, fabricante, voltagem, serial, tamanho, tipo, tempo)
            self.treeFerramenta.delete(*self.treeFerramenta.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
        except:
            print("Não foi possível fazer o cadastro")
#----------------------------------------------------------------------------------------------------------------------
# Método Limpar Tela
#----------------------------------------------------------------------------------------------------------------------
    def fLimparTela(self):
        try:
            self.txtCodigo.delete(0, END)
            self.txtDescricao.delete(0, END)
            self.txtFabricante.delete(0, END)
            self.txtVoltagem.delete(0, END)
            self.txtSerial.delete(0, END)
            self.txtTamanho.delete(0, END)
            self.txtTipo.delete(0, END)
            self.txtTempo.delete(0, END)
        except:
            print("Não foi possível Limpar os campos")
#-----------------------------------------------------------------------------------------------------------------------
# Método Excluir Tecnico
#-----------------------------------------------------------------------------------------------------------------------
    def fExcluirFerramenta(self):
        try:
            codigo, descricao, fabricante, voltagem, serial, tamanho, tipo, tempo = self.fLerCampos()
            self.objBD.excluirDados(codigo)
            # Recarrega dados na tela
            self.treeFerramenta.delete(*self.treeFerramenta.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
        except:
            print("Não foi possível fazer a exclusão")

#-----------------------------------------------------------------------------------------------------------------------
# Método Atualizar Tecnico
#-----------------------------------------------------------------------------------------------------------------------
    def fAtualizarFerramenta(self):
        try:
            codigo, descricao, fabricante, voltagem, serial, tamanho, tipo, tempo = self.fLerCampos()
            self.objBD.atualizarDados(codigo, descricao, fabricante, voltagem, serial, tamanho, tipo, tempo)
            # Recarrega dados na tela
            self.treeFerramenta.delete(*self.treeFerramenta.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
        except:
            print("Não foi possível fazer a atualização")
#-----------------------------------------------------------------------------------------------------------------------
# Método Gerar Excel
#-----------------------------------------------------------------------------------------------------------------------
    def fGerarExcel(self):
        try:
            self.Lista = self.objBD.selecionarDados()
            self.ListaFerramenta = pd.DataFrame(self.Lista, columns=["Codigo", "Descricao", "Fabricante", 'Voltagem',
                                                                     'Serial', 'Tamanho', 'Tipo', 'Tempo'])
            self.ListaFerramenta.to_excel('lista_ferramentas.xlsx')
            messagebox.showinfo(title="Alerta", message="Arquivo Criado com Sucesso!")
        except:
            print("Não foi possível criar o arquivo xlsx")





if __name__ == "__main__":
    janela = Tk()
    janela.geometry("930x650")
    janela.title('Bem Vindo a Aplicação de Banco de Dados')

    frame_ferramenta = Frame(janela, width=930, height=650)
    FerramentaBD(frame_ferramenta)

    frame_ferramenta.pack()


    janela.mainloop()
