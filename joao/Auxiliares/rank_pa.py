from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.collision import *
from PPlay.keyboard import *

def rank(janela):

	size = janela.height

	mouse = Window.get_mouse()
	keyboard = Window.get_keyboard()
	fundo = GameImage("Imagens/fundo_menu.png")
	botao1 = Sprite("Imagens/sair_pa.png")

	doc = open('scores.txt','r')
	players = doc.readlines()
	bests = [None]*5

	o1 = -1
	o2 = -1
	o3 = -1
	o4 = -1
	o5 = -1

	for i in range(len(players)):
		nome,score = players[i].split()
		score = int(score)
		if score > o1:
			o5 = o4
			o4 = o3
			o3 = o2
			o2 = o1
			
			bests.pop()

			o1 = score	
			bests = [str(nome + ': ' + str(score))] + bests 
		elif score > o2:
			o5 = o4
			o4 = o3
			o3 = o2
						
			bests.pop()
 
			o2 = score
			bests = bests[:1] + [nome + ': ' + str(score)] + bests[1:]
		elif score > o3:

			o5 = o4
			o4 = o3
			o3 = score

			bests.pop()

			bests = bests[:2] + [nome + ': ' + str(score)] + bests[2:] 
		elif score > o4:

			o5 = o4
			o4 = score

			bests.pop()

			bests = bests[:3] + [nome + ': ' + str(score)] + bests[3:] 
		elif score > o5:
			o5 = score
			bests[4] = nome + ' ' + str(score) 




	botao1.set_position(size/2,size/2 + 150)
	fundo.draw()
	botao1.draw()

	janela.update()

	while True:
		if mouse.is_over_object(botao1) and mouse.is_button_pressed(1):
			return 0


		fundo.draw()
		botao1.draw()
		cont = 0
		for i in range(5):

			janela.draw_text(str(bests[i]), size/2 + 50, 100 + cont , size=32, color=(250,250,250), font_name="Arial", bold=True, italic=False)
			cont += 50
		janela.update()

