from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.collision import *
from PPlay.keyboard import *
from random import randint

def luta(janela,dificuldade):
	size = janela.width
	mouse = Window.get_mouse()
	keyboard = Window.get_keyboard()

	life_enemy = 100
	life_player = 200
	pos_player = 1
	pos_enemy = 1
	time_hit = 1
	time_deu_hit = 0
	time_move = 0
	time_inicial = 0
	current_time = janela.delta_time()
	ja_apertou_mover = False
	ja_apertou_x = False
	tomou_dano = False
	deu_hit = False

	fundo = GameImage("Imagens/fundo_luta_agora_vai_phixr.png")

	#guarda = Sprite("Imagens/guarda_luta.png")
	guarda = Sprite("Imagens/guarda_luta_anim.png",2)
	guarda.set_total_duration(750)
	guarda.set_loop(True)
	barb = Sprite("Imagens/barbantinho_luta-export.png")
	#barb = Sprite("Imagens/chute_beta-export.png",2)
	#barb.set_total_duration(750)
	#barb.set_loop(True)
	barra = Sprite("Imagens/barra.png")
	vida = Sprite("Imagens/vida.png")

	vida = []
	for i in range(10):
		if i == 0:
			vida_pdc = Sprite("Imagens/vida_l.png")
		elif i == 9:
			vida_pdc = Sprite("Imagens/vida_rl.png")
		else:
			vida_pdc = Sprite("Imagens/vida.png")
		vida_pdc.set_position(50 + 90*i,40)
		vida_pdc.draw()
		vida.append(vida_pdc)

	fundo.set_position(-100,0)
	#fundo.set_position(0,0)
	guarda.set_position(size/2-100,size/2-250)
	barb.set_position(size/2-100,size/2-150)
	barra.set_position(50,40)         

	fundo.draw()
	guarda.draw()
	guarda.update()
	barb.draw()
	barra.draw()
	janela.update()

	while True:
		current_time += janela.delta_time()
		time_move += janela.delta_time()

		# delay inicial
		if time_inicial < 1:
			time_inicial += janela.delta_time()

		#chute
		if keyboard.key_pressed("x")and time_inicial > 0.9:
			if not ja_apertou_x:
				#alterar a animação
				barb = Sprite("Imagens/barbantinho_chute.png")
				barb.set_position(barb.x,size/2-250)
				if pos_player == pos_enemy:
					defende = randint(0,100)*dificuldade*(0.7)
					if defende >= 70:
						#animação de defesa
						guarda.set_position(guarda.x-100,guarda.y)	

					else:
						guarda = Sprite("Imagens/guarda_luta_dano.png",2)
						guarda.set_total_duration(750)
						guarda.set_loop(True)
						guarda.set_position(size/2 - pos_enemy*100,size/2-250)
						life_enemy -=30
						tomou_dano = True
						#print("Guarda",life_enemy)
						if life_enemy <= 0:
							return  10


				ja_apertou_x = True
		else:
			barb = Sprite("Imagens/barbantinho_luta-export.png")
			#barb.set_position(barb.x,size/2-150)
			if tomou_dano:
				guarda = Sprite("Imagens/guarda_luta_anim.png",2)
				guarda.set_total_duration(750)
				guarda.set_loop(True)
				guarda.set_position(size/2 - pos_enemy*100,size/2-250)
				tomou_dano = False
			
			ja_apertou_x = False


		if current_time >= time_hit/dificuldade and time_inicial > 0.9:
			atacar = randint(0,3)
			if atacar > 0 and pos_enemy == pos_player:
				life_player -= 40
				guarda = Sprite("Imagens/guarda_luta_hit-export.png",2)
				guarda.set_total_duration(750)
				guarda.set_loop(True)
				guarda.set_position(size/2 - pos_enemy*100,size/2-300)
				deu_hit = True
				if len(vida) > 0:
					vida.pop()
					vida.pop()
				if life_player <= 0:
					return 0

			current_time = 0

		if deu_hit == True:
			if time_deu_hit < 0.35:
				time_deu_hit += janela.delta_time()
			else:
				time_deu_hit = 0
				deu_hit = False
				if not tomou_dano:
					guarda =  Sprite("Imagens/guarda_luta_anim.png",2)
					guarda.set_total_duration(750)
					guarda.set_loop(True)
					guarda.set_position(size/2 - pos_enemy*100,size/2-250)


		if keyboard.key_pressed('left') or keyboard.key_pressed('a'):
			if not ja_apertou_mover:
				if pos_player <2:
					pos_player += 1
					ja_apertou_mover = True
		elif keyboard.key_pressed('right') or keyboard.key_pressed('d'):
			if not ja_apertou_mover:
				if pos_player > 0:
					pos_player -= 1
					ja_apertou_mover = True
		else:
			ja_apertou_mover = False


		if pos_player == 1:
			barb.set_position(size/2-100,size/2-150)
		elif pos_player == 2:
			barb.set_position(size/2-200,size/2-150)
		else:
			barb.set_position(size/2,size/2-150)

		if time_move >= 0.8:
			guarda.set_position(barb.x,size/2-250)
			pos_enemy = pos_player
			time_move = 0


			
		fundo.draw()
		guarda.draw()
		guarda.update()
		barb.draw()
		barra.draw()
		if len(vida) > 0:
			for pdc in vida:
				pdc.draw()
		janela.update()	


#size = 1000
#janela = Window(size,size)

#luta(janela,size,1)


def game_over(janela,score):
	mouse = Window.get_mouse()
	keyboard = Window.get_keyboard()
	size = janela.height
	fundo = GameImage("Imagens/fundo_menu.png")
	botao1 = Sprite("Imagens/sair_pa.png")
	over = GameImage("Imagens/game_over2.png")

	botao1.set_position(size/2,size/2 + 150)
	over.set_position(220,size/2 - 350)

	
	fundo.draw()
	over.draw()

	janela.update()


	while True:
		if mouse.is_over_object(botao1) and mouse.is_button_pressed(1):
			#janela.close()
			return 0


		fundo.draw()

		janela.draw_text(str("Score:"+ str(score)), 395, 362, size=52, color=(96,30,107), font_name="Arial", bold=True, italic=False)
		janela.draw_text(str("Score:"+ str(score)), 400, 360, size=50, color=(158,48,209), font_name="Arial", bold=True, italic=False)
		botao1.draw()
		over.draw()
		janela.update()


#janela = Window(1000,700)
#game_over(janela,70)