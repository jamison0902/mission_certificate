#----------------------------------------------------------------------------------------------------------------------
# Classes Reserva
#----------------------------------------------------------------------------------------------------------------------
from tkinter import *
from PIL import Image, ImageTk

class ReservaBD:
    def __init__(self, win):
        #self.objBD = crud.AppBD()

        # Inserindo Logo:
        self.image = Image.open('reserva.png').resize((70,70))
        self.photo = ImageTk.PhotoImage(self.image)
        self.labelImage = Label(win, image=self.photo)
        self.labelImage.image = self.photo
        self.labelImage.grid(row=0, column=0, columnspan=8, padx=10, pady=20)
        self.frase = Label(win, text='Nesta tela você pode cadastrar, excluir ou atualizar reservas.',
                           font=('arial', 12)).grid(row=1, column=0, columnspan=8, padx=10, pady=10)

        # Componente Label e Entrada de Dados
        self.lblFerramenta = Label(win, text='Ferramenta').grid(row=3, column=0, padx=5, pady=5)
        self.txtFerramenta = Entry(win).grid(row=3, column=1, padx=5, pady=5)

        self.lblDescricao = Label(win, text='Descrição').grid(row=3, column=2, padx=5, pady=5)
        self.txtDescricao = Entry(win).grid(row=3, column=3, padx=5, pady=5)

        self.lblData = Label(win, text='Data da Reserva').grid(row=3, column=4, padx=5, pady=5)
        self.txtData = Entry(win).grid(row=3, column=5, padx=5, pady=5)

        self.lblHoraR = Label(win, text='Hora da Retirada').grid(row=4, column=0, padx=5, pady=5)
        self.txtHoraR = Entry(win).grid(row=4, column=1, padx=5, pady=5)

        self.lblHoraD = Label(win, text='Hora da Devolução').grid(row=4, column=2, padx=5, pady=5)
        self.txtHoraD = Entry(win).grid(row=4, column=3, padx=5, pady=5)

        self.lblTecnico = Label(win, text='Técnico Responsável').grid(row=4, column=4, padx=5, pady=5)
        self.txtTecnico = Entry(win).grid(row=4, column=5, padx=5, pady=5)




if __name__ == "__main__":
    janela = Tk()
    janela.geometry("930x650")
    janela.title('Bem Vindo a Aplicação de Banco de Dados')

    frame_reserva = Frame(janela, width=930, height=650)
    ReservaBD(frame_reserva)

    frame_reserva.pack()


    janela.mainloop()
