"""
Created: 03/09/2022 11:54
@author: jamison.queiroz
Size: 5,39 kB
Type: Python
"""
#----------------------------------------------------------------------------------------------------------------------
# Classe Reserva
#----------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import pandas as pd
from tkinter import messagebox
import crud_reserva

class ReservaBD:
    def __init__(self, win):
        self.objBD = crud_reserva.AppBD()

        # Inserindo Logo:
        self.image = Image.open('reserva.png').resize((70,70))
        self.photo = ImageTk.PhotoImage(self.image)
        self.labelImage = Label(win, image=self.photo)
        self.labelImage.image = self.photo
        self.labelImage.grid(row=0, column=0, columnspan=8, padx=10, pady=20)
        self.frase = Label(win, text='Nesta tela você pode cadastrar, excluir ou atualizar reservas.',
                           font=('arial', 12)).grid(row=1, column=0, columnspan=8, padx=10, pady=10)

        # Componente Label e Entrada de Dados
        self.lblCodigo = Label(win, text='Código').grid(row=3, column=0, padx=5, pady=5)
        self.txtCodigo = Entry(win)
        self.txtCodigo.grid(row=3, column=1, padx=5, pady=5)

        self.lblFerramenta = Label(win, text='Ferramenta').grid(row=3, column=2, padx=5, pady=5)
        self.dicFerramenta = self.objBD.comboFerramenta()
        self.Ferramenta = StringVar()
        self.comboFerramenta = ttk.Combobox(win, values=list(self.dicFerramenta.values()), textvariable=self.Ferramenta)
        self.comboFerramenta.grid(row=3, column=3, padx=5, pady=5)

        self.lblTecnico = Label(win, text='Técnico').grid(row=3, column=4, padx=5, pady=5)
        self.dicTecnico = self.objBD.comboTecnico()
        self.Tecnico = StringVar()
        self.comboTecnico = ttk.Combobox(win, values=list(self.dicTecnico.values()), textvariable=self.Tecnico)
        self.comboTecnico.grid(row=3, column=5, padx=5, pady=5)

        self.lblData = Label(win, text='Data').grid(row=3, column=6, padx=5, pady=5)
        self.txtData = Entry(win)
        self.txtData.grid(row=3, column=7, padx=5, pady=5)

        self.lblHoraR = Label(win, text='Hora Retirada').grid(row=4, column=0, padx=5, pady=5)
        self.txtHoraR = Entry(win)
        self.txtHoraR.grid(row=4, column=1, padx=5, pady=5)

        self.lblHoraD = Label(win, text='Hora Devolução').grid(row=4, column=2, padx=5, pady=5)
        self.txtHoraD = Entry(win)
        self.txtHoraD.grid(row=4, column=3, padx=5, pady=5)

        self.lblDescricao = Label(win, text='Descrição').grid(row=4, column=4, padx=5, pady=5)
        self.txtDescricao = Entry(win, width=35)
        self.txtDescricao.grid(row=4, column=5, columnspan=2, padx=5, pady=5)

        # Botões
        self.btnCadastrar = Button(win, text='Cadastrar', command=self.fCadastrarReserva).grid(row=5, column=2, padx=5, pady=20)
        self.btnAtualizar = Button(win, text='Atualizar', command=self.fAtualizarReserva).grid(row=5, column=3, padx=5, pady=20)
        self.btnExcluir = Button(win, text='Excluir', command=self.fExcluirReserva).grid(row=5, column=4, padx=5, pady=20)
        self.btnLimpar = Button(win, text='Gerar Excel', command=self.fGerarExcel).grid(row=5, column=5, padx=5, pady=20)
        self.btnLimpar = Button(win, text='Limpar', command=self.fLimparTela).grid(row=5, column=6, padx=5, pady=20)

        # Componentes TreeView
        self.dadosColunas = ("Codigo", "Ferramenta", "Descricao", 'Data', 'Retirada', 'Devolucao', 'Tecnico')
        self.treeReserva = ttk.Treeview(win, columns=self.dadosColunas, show='headings')
        self.scrollbar = ttk.Scrollbar(win, orient=VERTICAL, command=self.treeReserva.yview())
        self.treeReserva.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=6, column=8, sticky='ns', padx=5, pady=5)

        self.treeReserva.heading("Codigo", text="Codigo")
        self.treeReserva.heading("Ferramenta", text="Ferramenta")
        self.treeReserva.heading("Descricao", text="Descrição")
        self.treeReserva.heading("Data", text="Data")
        self.treeReserva.heading("Retirada", text="Hora Retirada")
        self.treeReserva.heading("Devolucao", text="Hora Devolucao")
        self.treeReserva.heading("Tecnico", text="Tecnico")

        self.treeReserva.column("Codigo", minwidth=0, width=50)
        self.treeReserva.column("Ferramenta", minwidth=0, width=150)
        self.treeReserva.column("Descricao", minwidth=0, width=200)
        self.treeReserva.column("Data", minwidth=0, width=100)
        self.treeReserva.column("Retirada", minwidth=0, width=100)
        self.treeReserva.column("Devolucao", minwidth=0, width=100)
        self.treeReserva.column("Tecnico", minwidth=0, width=120)

        self.treeReserva.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)
        self.treeReserva.grid(row=6, column=0, columnspan=8, padx=5, pady=5)

        self.carregarDadosIniciais()

# ----------------------------------------------------------------------------------------------------------------------
# Método Apresentar Registro Selecionado
# ----------------------------------------------------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):
        self.fLimparTela()
        for selection in self.treeReserva.selection():
            item = self.treeReserva.item(selection)
            codigo, ferramenta_id, descricao, data, horar, horad, tecnico_id = item["values"][0:7]
            self.txtCodigo.insert(0, codigo)
            self.comboFerramenta.set(ferramenta_id)
            self.txtDescricao.insert(0, descricao)
            self.txtData.insert(0, data)
            self.txtHoraR.insert(0, horar)
            self.txtHoraD.insert(0, horad)
            self.comboTecnico.set(tecnico_id)

# ----------------------------------------------------------------------------------------------------------------------
# Método Carregar Dados Iniciais
# ----------------------------------------------------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
            self.iid = 0
            self.registros = self.objBD.selecionarDados()
            for item in self.registros:
                codigo = item[0]
                ferramenta_id = item[1]
                descricao = item[2]
                data = item[3]
                horar = item[4]
                horad = item[5]
                tecnico_id = item[6]
                self.treeReserva.insert('', 'end', iid=self.iid, values=(codigo, ferramenta_id, descricao, data,
                                                                         horar, horad, tecnico_id))
                self.iid = self.iid + 1
        except:
            print("Ainda não existem dados para carregar")
# ----------------------------------------------------------------------------------------------------------------------
# Método Ler Dados da Tela
# ----------------------------------------------------------------------------------------------------------------------
    def fLerCampos(self):
        try:
            codigo = int(self.txtCodigo.get())
            ferramenta_id = self.Ferramenta.get()
            descricao = self.txtDescricao.get()
            data = self.txtData.get()
            horar = self.txtHoraR.get()
            horad = self.txtHoraD.get()
            tecnico_id = self.Tecnico.get()
        except:
            print("Não foi possível ler os dados.")
        return codigo, ferramenta_id, descricao, data, horar, horad, tecnico_id
#----------------------------------------------------------------------------------------------------------------------
# Método Cadastrar Produto
#----------------------------------------------------------------------------------------------------------------------
    def fCadastrarReserva(self):
        try:

            ferramenta_id = self.Ferramenta.get()
            descricao = self.txtDescricao.get()
            data = self.txtData.get()
            horar = self.txtHoraR.get()
            horad = self.txtHoraD.get()
            tecnico_id = self.Tecnico.get()
            self.objBD.inserirDados(ferramenta_id, descricao, data, horar, horad, tecnico_id)
            self.treeReserva.delete(*self.treeReserva.get_children())
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
            self.comboFerramenta.set('')
            self.txtDescricao.delete(0, END)
            self.txtData.delete(0, END)
            self.txtHoraR.delete(0, END)
            self.txtHoraD.delete(0, END)
            self.comboTecnico.set('')
        except:
            print("Não foi possível Limpar os campos")
#-----------------------------------------------------------------------------------------------------------------------
# Método Excluir Tecnico
#-----------------------------------------------------------------------------------------------------------------------
    def fExcluirReserva(self):
        try:
            codigo, ferramenta_id, descricao, data, horar, horad, tecnico_id = self.fLerCampos()
            self.objBD.excluirDados(codigo)
            # Recarrega dados na tela
            self.treeReserva.delete(*self.treeReserva.get_children())
            self.carregarDadosIniciais()
            self.fLimparTela()
        except:
            print("Não foi possível fazer a exclusão")

#-----------------------------------------------------------------------------------------------------------------------
# Método Atualizar Tecnico
#-----------------------------------------------------------------------------------------------------------------------
    def fAtualizarReserva(self):
        try:
            codigo, ferramenta_id, descricao, data, horar, horad, tecnico_id = self.fLerCampos()
            self.objBD.atualizarDados(codigo, ferramenta_id, descricao, data, horar, horad, tecnico_id)
            # Recarrega dados na tela
            self.treeReserva.delete(*self.treeReserva.get_children())
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
            self.ListaReserva = pd.DataFrame(self.Lista, columns=["Codigo","Ferramenta", "Descricao", 'Data', 'Retirada',
                                                                   'Devolucao', 'tecnico'])
            self.ListaReserva.to_excel('lista_reserva.xlsx')
            messagebox.showinfo(title="Alerta", message="Arquivo Criado com Sucesso!")
        except:
            print("Não foi possível criar o arquivo xlsx")



if __name__ == "__main__":
    janela = Tk()
    janela.geometry("930x650")
    janela.title('Bem Vindo a Aplicação de Banco de Dados')
    frame_reserva = Frame(janela, width=930, height=650)
    ReservaBD(frame_reserva)
    frame_reserva.pack()
    janela.mainloop()
