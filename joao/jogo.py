from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

janela = Window(800, 500)
teclado = Window.get_keyboard()
mouse = Window.get_mouse()
janela.set_title("jogo")
janela.set_background_color((54, 63, 94))
bola = Sprite("bola.png")
barradireita = Sprite("barra direita.png")
barraesquerda = Sprite("barra esquerda.png")
bola.set_position(janela.width/2, janela.height/2)
pontobot = 0
pontogente = 0
velxbola = 150
velybola = 150
velybarradireita = 200
velybarraesquerda = 400
barradireita.set_position(janela.width*4.5/5, janela.height/2)
barraesquerda.set_position(janela.width/10, janela.height/2)
while True:
    janela.set_background_color((54, 63, 94))
    barraesquerda.draw()
    barradireita.draw()
    bola.y += velybola * janela.delta_time()
    bola.x += velxbola * janela.delta_time()
    janela.draw_text(str(pontogente), janela.width/4, janela.height/8, 50, (0, 0, 0), "arial", False, False)
    janela.draw_text(str(pontobot), janela.width*4/5, janela.height/8, 50, (0, 0, 0), "arial", False, False)
    bola.draw()
    if velxbola > 0:
        if velybola > 0:
            if bola.y > janela.height / 2:
                if barradireita.y < janela.height / 2:
                    barradireita.y += velybarradireita * janela.delta_time()
                else:
                    if barradireita.y != bola.y:
                        if barradireita.y > bola.y:
                            barradireita.y -= velybarradireita * janela.delta_time()
                        else:
                            barradireita.y += velybarradireita * janela.delta_time()
                    else:
                        barradireita.y = bola.y
            else:
                if barradireita.y < janela.height / 2:
                    if barradireita.y != bola.y:
                        if barradireita.y > bola.y:
                            barradireita.y -= velybarradireita * janela.delta_time()
                        else:
                            barradireita.y += velybarradireita * janela.delta_time()
                    else:
                        barradireita.y = bola.y
                else:
                    barradireita.y -= velybarradireita * janela.delta_time()
        else:
            if bola.y > janela.height / 2:
                if barradireita.y < janela.height / 2:
                    barradireita.y -= velybarradireita * janela.delta_time()
                else:
                    if barradireita.y != bola.y:
                        if barradireita.y > bola.y:
                            barradireita.y -= velybarradireita * janela.delta_time()
                        else:
                            barradireita.y += velybarradireita * janela.delta_time()
                    else:
                        barradireita.y = bola.y
            else:
                if barradireita.y < janela.height / 2:
                    if barradireita.y != bola.y:
                        if barradireita.y > bola.y:
                            barradireita.y -= velybarradireita * janela.delta_time()
                        else:
                            barradireita.y += velybarradireita * janela.delta_time()
                    else:
                        barradireita.y = bola.y
                else:
                    barradireita.y -= velybarradireita * janela.delta_time()
    if teclado.key_pressed("W"):
        barraesquerda.y -= velybarraesquerda * janela.delta_time()
    if teclado.key_pressed("S"):
        barraesquerda.y += velybarraesquerda * janela.delta_time()
    if barraesquerda.y <= 0:
        barraesquerda.y = 0
    elif barraesquerda.y >= janela.height - barraesquerda.height:
        barraesquerda.y = janela.height - barraesquerda.height
    if barradireita.y >= janela.height - barradireita.height:
        barradireita.y = janela.height - barradireita.height
    elif barradireita.y <= 0:
        barradireita.y = 0
    if bola.collided(barradireita):
        bola.x -= 1
        velxbola += 20
        velybola += 30
        velxbola *= -1
    if bola.collided(barraesquerda):
        bola.x += 1
        velxbola += 20
        velybola += 30
        velxbola *= -1
    if bola.x >= janela.width - bola.width or bola.x < 0:
        if bola.x < 0:
            pontobot += 1
        else:
            pontogente += 1
        bola.set_position(janela.width / 2, janela.height / 2)
    if bola.y >= janela.height - bola.height:
        bola.y = janela.height - bola.height
        velybola *= -1
    elif bola.y < 0:
        bola.y = 0
        velybola *= -1
    janela.update()
