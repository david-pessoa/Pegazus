#DESAFIO!!
#crie uma interface de banco, o programa deve utilizar POO, a classe deve ter os atributos id, nome, cpf e saldo , aonde o saldo deve ser iniciado em 0, e o id deve ser autoicremental. a interfaçe deve permitir a criação de uma conta, e a realização das operações de saque e deposito do saldo da conta

from cliente import Cliente
from tkinter import *
from PIL import Image, ImageDraw, ImageFont

BACKGROUND_COLOR = "#6877FF"
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#000000"
YELLOW_COLOR = "#FDBA38"
RED_COLOR = "#FF0000" #65%

window = Tk()
window.title("Banco do Python")
window.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)
#flip_timer = window.after(3000, show_english_translation)


canvas = Canvas(width= 800, height = 500)



canvas.config(bg= BACKGROUND_COLOR, highlightthickness= 0)
canvas.grid(row= 0, column= 0, columnspan= 2)

card_title = canvas.create_text(400, 150, text= "Title", font= ("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "word", font= ("Arial", 60, "bold"))


window.mainloop()

