from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from Auxiliares.luta_pa import *
from Auxiliares.paranaue_plataforma2 import *

def plataforma(janela, nome):

    teclado = Window.get_keyboard()



    player = Sprite("Imagens/player.png")
    fundo = Sprite("Imagens/foto1.png")
    guarda1 = Sprite("Imagens/inimigo.png")
    guarda2 = Sprite("Imagens/inimigo.png")
    plat = Sprite("Imagens/plat2.png")
    grama = Sprite("Imagens/grama.png")
    terra = Sprite("Imagens/terra.png")
    base_plat = Sprite("Imagens/platbase2.png")
    base_plat2 = Sprite("Imagens/platbase2.png")
    base_plat3 = Sprite("Imagens/platbase2.png")

    base_plat.set_position(0, janela.height - base_plat.height)
    base_plat2.set_position(base_plat.width, janela.height - base_plat2.height)
    base_plat3.set_position(janela.width - base_plat3.width, janela.height - base_plat3.height)
    plat.set_position(janela.width - base_plat3.width - 250, janela.height - base_plat3.height * 2 - plat.height)
    terra.set_position(janela.width - base_plat3.width - 250, janela.height - base_plat3.height * 2 - terra.height)
    grama.set_position(janela.width - base_plat3.width - 250, janela.height - base_plat3.height * 2 - terra.height - grama.height)
    player.set_position(0, janela.height - base_plat.height - player.height)
    guarda1.set_position(janela.width/1.5 - 80, janela.height - base_plat3.height * 2 - grama.height - terra.height - guarda1.height)

    

    g1 = 0
    velplayerx = 100
    delaypulo = 0
    delayandar = 100
    x = 0
    subindo = 0
    y = janela.height - base_plat.height - player.height
    pulo = 0
    respirarinimigo = 0
    movimento = 0
    velplayery = 300
    gravidade = 110
    clone = player
    score = 0
    lifes = 1


    direita = Sprite("Imagens/player.png")
    esquerda = Sprite("Imagens/-player.png")
    while True:
        fundo.draw()
        if player.collided(base_plat) or player.collided(base_plat2) or player.collided(base_plat3) or player.collided(grama):
            if teclado.key_pressed("SPACE"):
                pulo = 1
            if teclado.key_pressed("D") or teclado.key_pressed("right"):
                player.x += velplayerx * janela.delta_time()
                x += velplayerx * janela.delta_time()
                clone = direita
                if movimento == 0:
                    player = Sprite("Imagens/andar1.png")
                    movimento += 1
                    player.set_position(x, y)
                elif movimento <= 16:
                    player = Sprite("Imagens/andar2.png")
                    movimento += 1
                    player.set_position(x, y)
                elif movimento <= 32:
                    player = Sprite("Imagens/andar3.png")
                    movimento += 1
                    player.set_position(x, y)
                elif movimento <= 48:
                    player = Sprite("Imagens/andar4.png")
                    movimento += 1
                    player.set_position(x, y)
                elif movimento <= 64:
                    player = Sprite("Imagens/andar5.png")
                    movimento = 0
                    player.set_position(x, y)
            else:
                player = Sprite("Imagens/player.png")
                player.set_position(x, y)

            if teclado.key_pressed("A") or teclado.key_pressed("left"):
                player.x -= velplayerx * janela.delta_time()
                x -= velplayerx * janela.delta_time()
                clone = esquerda
                if movimento <= 0:
                    player = Sprite("Imagens/-andar1.png")
                    movimento += 1
                    player.set_position(x, y)
                elif movimento <= 16:
                    player = Sprite("Imagens/-andar2.png")
                    movimento += 1
                    player.set_position(x, y)
                elif movimento <= 32:
                    player = Sprite("Imagens/-andar3.png")
                    movimento += 1
                    player.set_position(x, y)
                elif movimento <= 48:
                    player = Sprite("Imagens/-andar4.png")
                    movimento += 1
                    player.set_position(x, y)
                elif movimento <= 64:
                    player = Sprite("Imagens/-andar5.png")
                    movimento = 0
                    player.set_position(x, y)
                if player.x < 0:
                    player.x = 0
        else:
            player.y += gravidade * janela.delta_time()
            y += gravidade * janela.delta_time()
        if pulo == 1:
            if subindo < 85:
                player.y -= velplayery * janela.delta_time()
                subindo += 1
                y -= velplayery * janela.delta_time()
                if clone == direita:
                    if movimento <= 0:
                        player = Sprite("Imagens/pular1.png")
                        movimento += 1
                        player.set_position(x, y)
                    elif movimento <= 32:
                        player = Sprite("Imagens/pular2.png")
                        movimento += 1
                        player.set_position(x, y)
                    elif movimento <= 64:
                        player = Sprite("Imagens/pular3.png")
                        movimento += 1
                        player.set_position(x, y)
                    elif movimento <= 96:
                        player = Sprite("Imagens/pular4.png")
                        movimento += 1
                        player.set_position(x, y)
                    elif movimento <= 128:
                        player = Sprite("Imagens/pular5.png")
                        player.set_position(x, y)
                elif clone == esquerda:
                    if movimento <= 0:
                        player = Sprite("Imagens/-pular1.png")
                        movimento += 1
                        player.set_position(x, y)
                    elif movimento <= 32:
                        player = Sprite("Imagens/-pular2.png")
                        movimento += 1
                        player.set_position(x, y)
                    elif movimento <= 64:
                        player = Sprite("Imagens/-pular3.png")
                        movimento += 1
                        player.set_position(x, y)
                    elif movimento <= 96:
                        player = Sprite("Imagens/-pular4.png")
                        movimento += 1
                        player.set_position(x, y)
                    elif movimento <= 128:
                        player = Sprite("Imagens/-pular5.png")
                        player.set_position(x, y)
            else:
                movimento = 0
                pulo = 0
                subindo = 0
        if teclado.key_pressed("D") or teclado.key_pressed("right"):
            player.x += velplayerx * janela.delta_time()
            x += velplayerx * janela.delta_time()
        if teclado.key_pressed("A") or teclado.key_pressed("left"):
            player.x -= velplayerx * janela.delta_time()
            x -= velplayerx * janela.delta_time()
        
        if y > base_plat.y:
            y = janela.height - base_plat.height - player.height


        if respirarinimigo <= 0:
            guarda1 = Sprite("Imagens/respirar inimigo.png")
            guarda1.set_position(janela.width / 1.5 - 80, janela.height - base_plat3.height * 2 - grama.height - terra.height - guarda1.height)
            respirarinimigo = 400
        elif respirarinimigo <= 200:
            guarda1 = Sprite("Imagens/inimigo.png")
            guarda1.set_position(janela.width / 1.5 - 80, janela.height - base_plat3.height * 2 - grama.height - terra.height - guarda1.height)
            respirarinimigo -= 1
        else:
            respirarinimigo -= 1


        if g1 == 0:
            if guarda1.x > player.x and guarda1.x < player.x + guarda1.height:
                if guarda1.collided(player):
                    n_score = luta(janela, 1)
                    if n_score == 0:
                        game_over(janela, score)
                        return 0
                    else:
                        score += n_score
                        g1 = 1
        if player.y > janela.height:
            doc = open("scores.txt",'a')
            doc.write(("{} {} \n").format(nome,score))
            doc.close()

            game_over(janela, score)
            return 0


        if player.x > janela.width:
            plataforma2(janela, nome, score)
            return 0

        base_plat2.draw()
        #plat.draw()
        terra.draw()
        grama.draw()
        base_plat.draw()
        base_plat3.draw()

        if g1 == 0:
           guarda1.draw()
        
        player.draw()
        janela.update()
