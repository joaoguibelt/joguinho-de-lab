from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *



def vitoria(janela, score):
    mouse = Window.get_mouse()
    keyboard = Window.get_keyboard()
    size = janela.height
    fundo = GameImage("fundo_menu.png")
    botao1 = Sprite("Imagens/sair_pa.png")
    over = GameImage("you_win.png")

    botao1.set_position(size / 2, size / 2 + 150)
    over.set_position(220, size / 2 - 350)

    fundo.draw()
    over.draw()

    janela.update()

    while True:
        if mouse.is_over_object(botao1) and mouse.is_button_pressed(1):
            # janela.close()
            return 0

        fundo.draw()

        janela.draw_text(str("Score:" + str(score)), 395, 362, size=52, color=(96, 30, 107), font_name="Arial",
                         bold=True, italic=False)
        janela.draw_text(str("Score:" + str(score)), 400, 360, size=50, color=(158, 48, 209), font_name="Arial",
                         bold=True, italic=False)
        botao1.draw()
        over.draw()
        janela.update()



