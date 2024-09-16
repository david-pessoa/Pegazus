#DESAFIO!!
#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta
from cliente import Cliente
from tkinter import *

BACKGROUND_COLOR = "#6877FF"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"
YELLOW_COLOR = "#FFD600"
RED_COLOR = "#FF0000" #65%

cliente_logado = None 
clientes = {}

CPF_input = None
Nome_input = None
Senha_input = None
Saque_input = None
Deposito_input = None
canvas = None

fez_deposito = False #Verifica se fez depósito
is_new_client = False #Verifica se é um novo usuário

def verifica_login():
    global cliente_logado
    global CPF_input
    global Senha_input
    global canvas
    
    cpf = CPF_input.get()
    senha = Senha_input.get()
    for id, cliente in clientes.items():
        if cliente.getCPF() == cpf and cliente.getSenha() == senha:
            tela_mostra_saldo()
        else:
            canvas.create_text(400, 350, fill= RED_COLOR, text= "Senha ou CPF incorretos!", font= ("Arial", 20))
    if clientes == {}:
        canvas.create_text(400, 350, fill= RED_COLOR, text= "Senha ou CPF incorretos!", font= ("Arial", 20))

def verifica_saque():
    global canvas
    global cliente_logado
    global Saque_input

    saque = float(Saque_input.get())
    saldo = cliente_logado.getSaldo()
    if cliente_logado.getSaldo() < saque:
        
        canvas.create_text(400, 400, fill= RED_COLOR, text= "Seu saldo de: R$ %.2f é insuficiente para realizar o saque" % cliente_logado.getSaldo(), font= ("Arial", 20))
    else:
        cliente_logado.saque(saque)
        tela_mostra_saldo()


            

########################################### TELA INICIAL #############################################################
def tela_inicial():
    global window
    global cliente_logado
    global CPF_input
    global Senha_input
    global canvas
    window.destroy()
    window = Tk()
    window.title("Banco do Python")
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500)


    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
    canvas.grid(row= 0, column= 0)

    canvas.create_text(400, 61, fill= WHITE_COLOR, text= "Banco do Python", font= ("Arial", 68, "bold"))
    canvas.create_text(318, 159, fill= BLACK_COLOR, text= "Digite seu CPF:", font= ("Arial", 30))

    CPF_input = Entry(width= 40)
    CPF_input.place(x= 400, y= 200, anchor= "center")

    canvas.create_text(327, 250, fill= BLACK_COLOR, text= "Digite sua senha:", font= ("Arial", 30))

    Senha_input = Entry(width= 40, show= '•')
    Senha_input.place(x= 400, y= 300, anchor= "center")


    cadastrar = Button(canvas, text="Cadastre-se", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_cadastro) #command= troca pra tela de cadastro
    cadastrar.place(x= 200, y= 400, anchor="center") # Verifique se aparece amarelo para você

    login = Button(canvas, text="Login", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= verifica_login)
    login.place(x= 600, y= 400) # Verifique se aparece amarelo para você

    window.mainloop()

####################################################### TELA CADASTRO #########################################################

def tela_cadastro():
    global window
    global cliente_logado
    global CPF_input
    global Nome_input
    global Senha_input
    global is_new_client
    is_new_client = True
    window.destroy()
    window = Tk() 
    window.title("Banco do Python")
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500)


    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
    canvas.grid(row= 0, column= 0)

    canvas.create_text(400, 61, fill= WHITE_COLOR, text= "Crie uma conta", font= ("Arial", 68, "bold"))

    canvas.create_text(318, 125, fill= BLACK_COLOR, text= "Digite seu Nome:", font= ("Arial", 30))
    Nome_input = Entry(width= 40)
    Nome_input.place(x= 400, y= 175, anchor= "center")

    canvas.create_text(318, 225, fill= BLACK_COLOR, text= "Digite seu CPF:", font= ("Arial", 30))

    CPF_input = Entry(width= 40)
    CPF_input.place(x= 400, y= 275, anchor= "center")


    canvas.create_text(318, 325, fill= BLACK_COLOR, text= "Crie uma senha:", font= ("Arial", 30))

    Senha_input = Entry(width= 40, show= '•')
    Senha_input.place(x= 400, y= 375, anchor= "center")

    cadastrar = Button(canvas, text="Criar cadastro", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_mostra_saldo)
    cadastrar.place(x= 200, y= 450) # Verifique se aparece amarelo para você

######################################################### TELA MOSTRA SALDO ############################################################

def tela_mostra_saldo():
    global window
    global cliente_logado
    global Nome_input
    global CPF_input
    global Senha_input
    global is_new_client
    global Deposito_input
    global fez_deposito

    if is_new_client:
        cliente_logado = Cliente(Nome_input.get(), CPF_input.get(), Senha_input.get())
        clientes[cliente_logado.getId()] = cliente_logado
        is_new_client = False
    
    if fez_deposito:
        deposito = float(Deposito_input.get())
        cliente_logado.deposito(deposito)
        fez_deposito = False

    window.destroy()
    window = Tk() 
    window.title("Banco do Python")
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500)

    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
    canvas.grid(row= 0, column= 0)

    canvas.create_text(400, 61, fill= WHITE_COLOR, text= f"Bem vindo, {cliente_logado.getNome()}!", font= ("Arial", 60, "bold"))

    canvas.create_text(400, 250, fill= YELLOW_COLOR, text= "Seu saldo: R$ %.2f" % cliente_logado.getSaldo(), font= ("Arial", 48, "bold"))
   

    sacar = Button(canvas, text="Sacar", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_de_saques)
    sacar.place(x= 150, y= 450) # Verifique se aparece amarelo para você

    depositar = Button(canvas, text="Depositar", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_de_depositos)
    depositar.place(x= 600, y= 450) # Verifique se aparece amarelo para você

###################################################### TELA PARA REALIZAR SAQUES #################################################

def tela_de_saques():
    global window
    global cliente_logado
    global Saque_input
    global canvas
    window.destroy()
    window = Tk() 
    window.title("Banco do Python")
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500)

    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
    canvas.grid(row= 0, column= 0)

    canvas.create_text(400, 61, fill= WHITE_COLOR, text= f"Digite o valor a ser sacado", font= ("Arial", 60, "bold"))

    canvas.create_text(200, 250, fill= BLACK_COLOR, text= "R$", font= ("Arial", 48, "bold"))
    Saque_input = Entry(width= 15, font= ("Arial", 48, "bold"))
    Saque_input.place(x= 300, y= 220)
   

    sacar = Button(canvas, text="Sacar", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= verifica_saque)
    sacar.place(x= 150, y= 450) # Verifique se aparece amarelo para você


################################################################# TELA PARA REALIZAR DEPÓSITOS ####################################

def tela_de_depositos():
    global window
    global cliente_logado
    global canvas
    global fez_deposito
    global Deposito_input
    window.destroy()
    window = Tk() 
    window.title("Banco do Python")
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500)

    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
    canvas.grid(row= 0, column= 0)

    canvas.create_text(400, 61, fill= WHITE_COLOR, text= f"Digite o valor a ser depositado", font= ("Arial", 50, "bold"))

    canvas.create_text(200, 250, fill= BLACK_COLOR, text= "R$", font= ("Arial", 48, "bold"))
    Deposito_input = Entry(width= 15, font= ("Arial", 48, "bold"))
    Deposito_input.place(x= 300, y= 220)
   

    sacar = Button(canvas, text="Depositar", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_mostra_saldo)
    sacar.place(x= 150, y= 450) # Verifique se aparece amarelo para você

    fez_deposito = True



window = Tk()
tela_inicial()
window.mainloop()