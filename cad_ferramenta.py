#----------------------------------------------------------------------------------------------------------------------
# Classes Ferramenta
#----------------------------------------------------------------------------------------------------------------------
from tkinter import *
from PIL import Image, ImageTk

class FerramentaBD:
    def __init__(self, win):
        #self.objBD = crud.AppBD()

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
        self.txtCdigo = Entry(win).grid(row=3, column=1, padx=5, pady=5)

        self.lblDescricao = Label(win, text='Descrição').grid(row=3, column=2, padx=5, pady=5)
        self.txtDescricao = Entry(win).grid(row=3, column=3, padx=5, pady=5)

        self.lblFabricante = Label(win, text='Fabricante').grid(row=3, column=4, padx=5, pady=5)
        self.txtFabricante = Entry(win).grid(row=3, column=5, padx=5, pady=5)

        self.lblVoltagem = Label(win, text='Voltagem').grid(row=3, column=6, padx=5, pady=5)
        self.txtVoltagem = Entry(win).grid(row=3, column=7, padx=5, pady=5)

        self.lblSerial = Label(win, text='N. Serial').grid(row=4, column=0, padx=5, pady=5)
        self.txtSerial = Entry(win).grid(row=4, column=1, padx=5, pady=5)

        self.lblTamanho = Label(win, text='Tamanho').grid(row=4, column=2, padx=5, pady=5)
        self.txtTamanho = Entry(win).grid(row=4, column=3, padx=5, pady=5)

        self.lblTipo = Label(win, text='Tipo Ferramenta').grid(row=4, column=4, padx=5, pady=5)
        self.txtTipo = Entry(win).grid(row=4, column=5, padx=5, pady=5)

        self.lblTempo = Label(win, text='Tempo de Reserva').grid(row=4, column=6, padx=5, pady=5)
        self.txtTempo = Entry(win).grid(row=4, column=7, padx=5, pady=5)

# ----------------------------------------------------------------------------------------------------------------------
# Método Cadastrar Produto
# ----------------------------------------------------------------------------------------------------------------------
    def fCadastrarProduto(self):
        try:
            print("*****************  Dados disponíveis  **********************")
            codigo, nome, preco, = self.fLerCampos()
            self.objBD.inserirDados(codigo, nome, preco)
            self.treeProdutos.insert('', 'end', iid=self.iid, values=(codigo, nome, preco))
            self.iid = self.iid + 1
            self.id += 1
            print('Produto Cadastrado com Sucesso!')
        except:
            print("Não foi possível fazer o cadastro")






if __name__ == "__main__":
    janela = Tk()
    janela.geometry("930x650")
    janela.title('Bem Vindo a Aplicação de Banco de Dados')

    frame_ferramenta = Frame(janela, width=930, height=650)
    FerramentaBD(frame_ferramenta)

    frame_ferramenta.pack()


    janela.mainloop()
