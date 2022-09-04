from tkinter import *
from tkinter import messagebox
import cad_tecnico
import cad_ferramenta
import cad_reserva

def go_tecnico():
    cad_tecnico.TecnicoBD(frame_tecnico)
    frame_tecnico.pack()
    frame_ferramenta.pack_forget()
    frame_reserva.pack_forget()

def go_ferramenta():
    cad_ferramenta.FerramentaBD(frame_ferramenta)
    frame_ferramenta.pack()
    frame_reserva.pack_forget()
    frame_tecnico.pack_forget()

def go_reserva():
    cad_reserva.ReservaBD(frame_reserva)
    frame_reserva.pack()
    frame_tecnico.pack_forget()
    frame_ferramenta.pack_forget()

def mensagem_alerta():
    messagebox.showinfo(title="Alerta", message="Testando")

principal = Tk()
principal.title('Sistema de Empréstimo de Ferramenta')
principal.geometry("940x600")

frame_tecnico = Frame(principal)
frame_ferramenta = Frame(principal)
frame_reserva = Frame(principal)


menubar = Menu(principal)
cadastrar = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Cadastrar', menu=cadastrar)
cadastrar.add_command(label ='Técnico', command=go_tecnico)
cadastrar.add_command(label ='Ferramenta', command=go_ferramenta)
reservar = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Reservar', menu=reservar)
reservar.add_command(label ='Ferramenta', command=go_reserva)
principal.config(menu=menubar)


principal.mainloop()