from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
def modoo():
        janela = Window(800, 450)
        janela.set_title("space invaders")
        fundo = GameImage("estrelas 8bit.jpg")
        facil = Sprite("facil.png")
        medio = Sprite("medio.png")
        dificil = Sprite("dificil.png")
        mouse = Window.get_mouse()
        bola = Sprite("bola.png")
        teclado = Window.get_keyboard()
        facil.set_position(janela.width / 2.4, janela.height / 8)
        medio.set_position(janela.width / 2.4, janela.height / 3)
        dificil.set_position(janela.width / 2.4, janela.height / 1.8)
        bola.set_position(janela.width/1.85, janela.height/1.6)
        while True:
                fundo.draw()
                if mouse.is_over_area((janela.width / 2.4, janela.height / 8), (janela.width / 1.85, janela.height / 5)) and mouse.is_button_pressed(1): #facil
                        return "facil"
                if mouse.is_over_area((janela.width / 2.4, janela.height / 8), (janela.width / 1.85, janela.height / 2.46)) and mouse.is_button_pressed(1):# medio
                        return "medio"
                if mouse.is_over_area((janela.width / 2.4, janela.height / 8), (janela.width / 1.85, janela.height / 1.6)) and mouse.is_button_pressed(1):# dificil
                        return "dificil"
                if teclado.key_pressed("esc"):
                        return None
                facil.draw()
                medio.draw()
                dificil.draw()
                bola.draw()
                janela.update()
