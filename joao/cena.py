from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.collision import *
from PPlay.keyboard import *
from random import randint

def luta(janela,dificuldade):
	mouse = Window.get_mouse()
	keyboard = Window.get_keyboard()

	life_enemy = 100
	life_player = 200
	pos_player = 1
	pos_enemy = 1
	time_hit = 1.5
	time_deu_hit = 0
	time_move = 0
	time_inicial = 0
	current_time = janela.delta_time()
	ja_apertou_mover = False
	ja_apertou_x = False
	tomou_dano = False
	deu_hit = False

	fundo = GameImage("fundo_luta_agora_vai_phixr.png")

	#guarda = Sprite("guarda_luta.png")
	guarda = Sprite("guarda_luta_anim.png",2)
	guarda.set_total_duration(750)
	guarda.set_loop(True)
	barb = Sprite("barbantinho_luta-export.png")
	#barb = Sprite("chute_beta-export.png",2)
	#barb.set_total_duration(750)
	#barb.set_loop(True)
	barra = Sprite("barra.png")
	vida = Sprite("vida.png")

	vida = []
	for i in range(10):
		if i == 0:
			vida_pdc = Sprite("vida_l.png")
		elif i == 9:
			vida_pdc = Sprite("vida_rl.png")
		else:
			vida_pdc = Sprite("vida.png")
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
				barb = Sprite("barbantinho_chute.png")
				barb.set_position(barb.x,size/2-250)
				if pos_player == pos_enemy:
					defende = randint(0,100)*dificuldade
					if defende >= 70:
						#animação de defesa
						print("defendeu")
						guarda.set_position(guarda.x-100,guarda.y)	

					else:
						guarda = Sprite("guarda_luta_dano.png",2)
						guarda.set_total_duration(750)
						guarda.set_loop(True)
						guarda.set_position(size/2 - pos_enemy*100,size/2-250)
						life_enemy -=30
						tomou_dano = True
						print("Guarda",life_enemy)
						if life_enemy <= 0:
							print("You Win")

				ja_apertou_x = True
		else:
			barb = Sprite("barbantinho_luta-export.png")
			#barb.set_position(barb.x,size/2-150)
			if tomou_dano:
				guarda = Sprite("guarda_luta_anim.png",2)
				guarda.set_total_duration(750)
				guarda.set_loop(True)
				guarda.set_position(size/2 - pos_enemy*100,size/2-250)
				tomou_dano = False
			
			ja_apertou_x = False


		if current_time >= time_hit and time_inicial > 0.9:
			atacar = randint(0,1)
			if atacar and pos_enemy == pos_player:
				life_player -= 40
				guarda = Sprite("guarda_luta_hit-export.png",2)
				guarda.set_total_duration(750)
				guarda.set_loop(True)
				guarda.set_position(size/2 - pos_enemy*100,size/2-300)
				deu_hit = True
				if len(vida) > 0:
					vida.pop()
					vida.pop()
				if life_player <= 0:
					print("Game Over!")
				print("Player:",life_player)

			current_time = 0

		if deu_hit == True:
			if time_deu_hit < 0.35:
				time_deu_hit += janela.delta_time()
			else:
				time_deu_hit = 0
				deu_hit = False
				if not tomou_dano:
					guarda =  Sprite("guarda_luta_anim.png",2)
					guarda.set_total_duration(750)
					guarda.set_loop(True)
					guarda.set_position(size/2 - pos_enemy*100,size/2-250)


		if keyboard.key_pressed('left') or keyboard.key_pressed('d'):
			if not ja_apertou_mover:
				if pos_player <2:
					pos_player += 1
					ja_apertou_mover = True
		elif keyboard.key_pressed('right') or keyboard.key_pressed('a'):
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


size = 1000
janela = Window(size,size)

luta(janela,1)

