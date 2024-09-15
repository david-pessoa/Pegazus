#DESAFIO!!
#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta
from itertools import tee
from cliente import Cliente
from tkinter import *

BACKGROUND_COLOR = "#6877FF"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"
YELLOW_COLOR = "#FDBA38"
RED_COLOR = "#FF0000" #65%

def tela_inicial():
    global window
    window.destroy()
    window = Tk()
    window.title("Banco do Python")
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500)


    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
    canvas.grid(row= 0, column= 0)

    title_text = canvas.create_text(400, 61, fill= WHITE_COLOR, text= "Banco do Python", font= ("Arial", 68, "bold"))
    digite_cpf_text = canvas.create_text(318, 159, fill= BLACK_COLOR, text= "Digite seu CPF:", font= ("Arial", 30))

    CPF_input = Entry(width= 40)
    CPF_input.place(x= 400, y= 200, anchor= "center")

    digite_senha_text = canvas.create_text(327, 250, fill= BLACK_COLOR, text= "Digite sua senha:", font= ("Arial", 30))

    Senha_input = Entry(width= 40)
    Senha_input.place(x= 400, y= 300, anchor= "center")

    cadastrar = Button(canvas, text="Cadastre-se", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_dois) #command= troca pra tela de cadastro
    cadastrar.place(x= 400, y= 400, anchor="center") # Verifique se aparece amarelo para você

    window.mainloop()

def tela_cadastro():
    global window
    window.destroy()
    window = Tk() 
    # Continuar

def tela_mostra_saldo():
    global window
    window.destroy()
    window = Tk() 
    # Continuar

def tela_de_saques():
    global window
    window.destroy()
    window = Tk() 
    # Continuar

def tela_de_depositos():
    global window
    window.destroy()
    window = Tk() 
    # Continuar



window = Tk()
tela_inicial()
window.mainloop()