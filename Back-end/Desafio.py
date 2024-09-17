from cliente import Cliente
from tkinter import *

# Cores utilizadas
BACKGROUND_COLOR = "#6877FF" # Cor ROXA para o fundo da tela
WHITE_COLOR = "#FFFFFF" # Cor BRANCA para a fonte do título da tela
BLACK_COLOR = "#000000" # Cor preta para texto
YELLOW_COLOR = "#FFD600" # Cor amarela para botões
RED_COLOR = "#FF0000" #65% # Cor vermelha para exibir erros

cliente_logado = None # variável global para guardar o cliente que está logado
clientes = {} # dicionário de clientes contendo como chave o id do cliente e como valor o objeto de Cliente()

CPF_input = None # Variáveis globais para guardar inputs das Entrys()
Nome_input = None
Senha_input = None
Saque_input = None
Deposito_input = None
canvas = None # Variável global para o canvas

fez_deposito = False #Verifica se fez depósito
is_new_client = False #Verifica se é um novo usuário

def verifica_login(): # Função para verificar se login está correto
    global cliente_logado
    global CPF_input # Chama variáveis globais
    global Senha_input
    global canvas
    
    cpf = CPF_input.get() #Obtém CPF e senha digitados na tela de login
    senha = Senha_input.get()
    for id, cliente in clientes.items(): #Verifica se, dentro do diocionário de clientes, há um cliente com o cpf e senha especificados
        if cliente.getCPF() == cpf and cliente.getSenha() == senha: # Se há um cliente com o CPF e senha especificados:
            cliente_logado = cliente # Define cliente_logado como o cliente que foi encontrado
            tela_mostra_saldo() #Vai para a tela mostra_saldo
        else:
            canvas.create_text(400, 350, fill= RED_COLOR, text= "Senha ou CPF incorretos!", font= ("Arial", 20)) # Senão, permanece na tela de login e exibe mensagem de erro
    if clientes == {}:
        canvas.create_text(400, 345, fill= RED_COLOR, text= "Não há clientes cadastrados, cadastre-se!", font= ("Arial", 20)) #Se não existe nenhum cliente logado, também exibe mensagem de erro

def verifica_saque(): #Função para verificar se o valor do saque é válido (menor ou igual ao saldo)
    global canvas
    global cliente_logado # Chama variáveis globais
    global Saque_input

    saque = float(Saque_input.get()) # Obtém saque e saldo
    saldo = cliente_logado.getSaldo()
    if cliente_logado.getSaldo() < saque: # Se o saque é maior que o saldo exibe mensagem de erro
        canvas.create_text(400, 400, fill= RED_COLOR, text= "Seu saldo de: R$ %.2f é insuficiente para realizar o saque" % cliente_logado.getSaldo(), font= ("Arial", 20))
    else:
        cliente_logado.saque(saque) #Senão, realiza o saque o volta para a tela que exibe o saldo
        tela_mostra_saldo()


            

########################################### TELA INICIAL #############################################################
def tela_inicial():
    global window
    global cliente_logado # Chama variáveis globais
    global CPF_input
    global Senha_input
    global canvas
    window.destroy() #Destrói janela anterior
    window = Tk() # Cria nova janela para a tela inicial
    window.title("Banco do Python") # Coloca título da tela
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR) #Define padding e cor de fundo ROXO
    canvas = Canvas(width= 800, height = 500) # Inicia canvas de 500px X 800px


    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0) #Define cor de fundo do canvas para ROXO e retira borda
    canvas.grid(row= 0, column= 0) #Coloca o canvas na posição (0,0) da grade

    canvas.create_text(400, 61, fill= WHITE_COLOR, text= "Banco do Python", font= ("Arial", 68, "bold")) #Coloca título da tela
    canvas.create_text(318, 159, fill= BLACK_COLOR, text= "Digite seu CPF:", font= ("Arial", 30)) # Coloca texto exigindo CPF para login

    CPF_input = Entry(width= 40) # Coloca input para o CPF
    CPF_input.place(x= 400, y= 200, anchor= "center")

    canvas.create_text(327, 250, fill= BLACK_COLOR, text= "Digite sua senha:", font= ("Arial", 30)) # Coloca texto exigindo senha da conta

    Senha_input = Entry(width= 40, show= '•') # Coloca senha para input da senha e substitui caracteres por '•'
    Senha_input.place(x= 400, y= 300, anchor= "center")

    #Cria botão cadastrar amarelo (em teoria) sem borda e que encaminha para a tela de cadastro
    cadastrar = Button(canvas, text="Cadastre-se", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_cadastro) #command= troca pra tela de cadastro
    cadastrar.place(x= 200, y= 400, anchor="center") # Verifique se aparece amarelo para você

    login = Button(canvas, text="Login", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= verifica_login) # Cria botão de login que verifica se os dados cadastrais digitados estão corretos
    login.place(x= 600, y= 400) # Verifique se aparece amarelo para você

    window.mainloop() # Mantém a tela aberta

####################################################### TELA CADASTRO #########################################################

def tela_cadastro():
    global window
    global cliente_logado
    global CPF_input # Chama variáveis globais
    global Nome_input
    global Senha_input
    global is_new_client
    is_new_client = True # Define usuário como novo usuário
    window.destroy() #Destrói janela anterior
    window = Tk() 
    window.title("Banco do Python") # Cria nova janela com as mesmas configurações
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500)

    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0) # Recria canva igual
    canvas.grid(row= 0, column= 0)

    canvas.create_text(400, 61, fill= WHITE_COLOR, text= "Crie uma conta", font= ("Arial", 68, "bold")) # Define o título da tela

    canvas.create_text(318, 125, fill= BLACK_COLOR, text= "Digite seu Nome:", font= ("Arial", 30)) # Coloca texto exigindo o nome do novo usuário
    Nome_input = Entry(width= 40) # Input para obter nome do novo usuário
    Nome_input.place(x= 400, y= 175, anchor= "center")

    canvas.create_text(318, 225, fill= BLACK_COLOR, text= "Digite seu CPF:", font= ("Arial", 30)) # Coloca texto exigindo o CPF do novo usuário

    CPF_input = Entry(width= 40) # Input para obter CPF do usuário
    CPF_input.place(x= 400, y= 275, anchor= "center")

    canvas.create_text(318, 325, fill= BLACK_COLOR, text= "Crie uma senha:", font= ("Arial", 30)) # Cria texto exigindo uma senha

    Senha_input = Entry(width= 40, show= '•') # Coloca input para obter senha do novo usuário, substituindo o caractere digitado por '•'
    Senha_input.place(x= 400, y= 375, anchor= "center")

    cadastrar = Button(canvas, text="Criar cadastro", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_mostra_saldo) # Coloca botão para criar cadastro
    cadastrar.place(x= 200, y= 450) # Verifique se aparece amarelo para você

######################################################### TELA MOSTRA SALDO ############################################################

def tela_mostra_saldo():
    global window
    global cliente_logado
    global Nome_input
    global CPF_input # chama variáveis globais
    global Senha_input
    global is_new_client
    global Deposito_input
    global fez_deposito

    if is_new_client: #Se é novo cliente obtém dados obtidos dos inputs da tela de cadastro e cria novo cliente
        cliente_logado = Cliente(Nome_input.get(), CPF_input.get(), Senha_input.get())
        clientes[cliente_logado.getId()] = cliente_logado
        is_new_client = False
    
    if fez_deposito: # Se o cliente acabou de fazer um depósito, atualiza saldo
        deposito = float(Deposito_input.get())
        cliente_logado.deposito(deposito)
        fez_deposito = False

    window.destroy() #Destrói janela anterior
    window = Tk() 
    window.title("Banco do Python") # Recria nova janela
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500)

    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0) # Recria canvas
    canvas.grid(row= 0, column= 0)
    # Coloca título na tela
    canvas.create_text(400, 61, fill= WHITE_COLOR, text= f"Bem vindo, {cliente_logado.getNome()}!", font= ("Arial", 60, "bold"))
    # Exibe saldo do cliente em preto
    canvas.create_text(400, 250, fill= BLACK_COLOR, text= "Seu saldo: R$ %.2f" % cliente_logado.getSaldo(), font= ("Arial", 48, "bold"))
   
    #Coloca botão para sacar dinheiro
    sacar = Button(canvas, text="Sacar", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_de_saques)
    sacar.place(x= 150, y= 450) # Verifique se aparece amarelo para você
    # Coloca botão para depositar dinheiro
    depositar = Button(canvas, text="Depositar", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_de_depositos)
    depositar.place(x= 600, y= 450) # Verifique se aparece amarelo para você

###################################################### TELA PARA REALIZAR SAQUES #################################################

def tela_de_saques():
    global window
    global cliente_logado # chama variáveis globais
    global Saque_input
    global canvas
    window.destroy() # destrói janela anterior
    window = Tk() 
    window.title("Banco do Python") #Recria janela
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500)

    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0) #Recria canvas
    canvas.grid(row= 0, column= 0)
    # Coloca texto exigindo o valor a ser sacado
    canvas.create_text(400, 61, fill= WHITE_COLOR, text= f"Digite o valor a ser sacado", font= ("Arial", 60, "bold")) 

    canvas.create_text(200, 250, fill= BLACK_COLOR, text= "R$", font= ("Arial", 48, "bold"))
    Saque_input = Entry(width= 15, font= ("Arial", 48, "bold")) # Coloca input para colocar o valor do saque
    Saque_input.place(x= 300, y= 220)
   
    # Coloca botão para realizar saque
    sacar = Button(canvas, text="Sacar", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= verifica_saque)
    sacar.place(x= 150, y= 450) # Verifique se aparece amarelo para você


################################################################# TELA PARA REALIZAR DEPÓSITOS ####################################

def tela_de_depositos():
    global window
    global cliente_logado
    global canvas
    global fez_deposito # Chama variáveis globais
    global Deposito_input
    window.destroy() #Destrói jnbela
    window = Tk() 
    window.title("Banco do Python") # Recria nova janela para depósitos
    window.config(padx= 10, pady= 10, bg= BACKGROUND_COLOR)
    canvas = Canvas(width= 800, height = 500) # Recria canvas

    canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
    canvas.grid(row= 0, column= 0)
    # Coloca texto solicitando o valor do depósito
    canvas.create_text(400, 61, fill= WHITE_COLOR, text= f"Digite o valor a ser depositado", font= ("Arial", 50, "bold"))

    canvas.create_text(200, 250, fill= BLACK_COLOR, text= "R$", font= ("Arial", 48, "bold"))
    Deposito_input = Entry(width= 15, font= ("Arial", 48, "bold")) #Coloca input para o valor do depósito
    Deposito_input.place(x= 300, y= 220)
   
    # Coloca botão para realizar depósito
    sacar = Button(canvas, text="Depositar", bg= YELLOW_COLOR, fg= BLACK_COLOR, font=("Arial", 30), highlightthickness= 0, command= tela_mostra_saldo)
    sacar.place(x= 150, y= 450) # Verifique se aparece amarelo para você

    fez_deposito = True # Indica que cliente realizou o depósito



window = Tk() # Cria variável global window para janela do Tk()
tela_inicial() # Chama tela inicial
window.mainloop() # Coloca em loop, para a interface gráfica não fechar
