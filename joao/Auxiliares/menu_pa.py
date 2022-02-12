from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.collision import *
from PPlay.keyboard import *
from Auxiliares.paranaue_plataforma import *
from Auxiliares.rank_pa import *
def Menu():

	nome = input("Digite o seu nome (sem espaços): ")

	size = 1000
	janela = Window(size,700)
	mouse = Window.get_mouse()
	keyboard = Window.get_keyboard()
	dificuldade = 1
	
	mouse = Window.get_mouse()
	keyboard = Window.get_keyboard()

	fundo = GameImage("Imagens/fundo_menu.png")
	botao1 = Sprite("Imagens/jogar_pa.png")
	botao2 = Sprite("Imagens/rank_pa.png")
	botao4 = Sprite("Imagens/sair_pa.png")
	logo = Sprite("Imagens/logo.png")

	logo.set_position(size/7, size*(3/100))
	botao1.set_position(size/2.9,size*(30/100))
	botao2.set_position(size/2.9,size*(45 /100)-10)
	botao4.set_position(size/2.9,size*(58/100))

	fundo.draw()
	botao1.draw()
	botao2.draw()
	botao4.draw()
	logo.draw()
	janela.update()

	



	while True:

		if mouse.is_over_object(botao1) and mouse.is_button_pressed(1):
			plataforma(janela,nome)
		if mouse.is_over_object(botao2) and mouse.is_button_pressed(1):
			rank(janela)
		
		if mouse.is_over_object(botao4) and mouse.is_button_pressed(1):
			janela.close()
			
		fundo.draw()
		botao1.draw()
		botao2.draw()
		botao4.draw()
		logo.draw()
		janela.update()
		



		janela.update()



