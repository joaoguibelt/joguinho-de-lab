from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from Auxiliares.luta_pa import *
from Auxiliares.vitoria import *

def plataforma3(janela, nome, score):
    teclado = Window.get_keyboard()

    bandeira = Sprite("Imagens/bandeira.png")
    player = Sprite("Imagens/player.png")
    fundo = Sprite("Imagens/foto1.png")
    guarda1 = Sprite("Imagens/inimigo.png")
    guarda2 = Sprite("Imagens/inimigo.png")
    guarda3 = Sprite("Imagens/inimigo.png")
    plat1 = Sprite("Imagens/plat2.png")
    grama1 = Sprite("Imagens/grama.png")
    grama2 = Sprite("Imagens/grama.png")
    grama3 = Sprite("Imagens/grama.png")
    terra1 = Sprite("Imagens/terra.png")
    terra2 = Sprite("Imagens/terra.png")
    terra3 = Sprite("Imagens/terra.png")
    base_plat = Sprite("Imagens/platbase2.png")
    base_grama1 = Sprite("Imagens/platbase3.png")
    base_plat2 = Sprite("Imagens/platbase2.png")
    #base_plat3 = Sprite("Imagens/platbase2.png")



    base_plat.set_position(0, janela.height - base_plat.height)
    # base_plat2.set_position(base_plat.width, janela.height - base_plat2.height)
    #base_plat3.set_position(janela.width - base_plat3.width, janela.height - base_plat3.height)
    base_grama1.set_position(janela.width - base_grama1.width, janela.height - base_grama1.height)
    plat1.set_position(base_plat.width + plat1.width - 100, janela.height - base_plat.height * 2 - plat1.height)
    terra1.set_position(janela.width - base_plat.width - 250, janela.height - base_plat.height * 2 - terra1.height - 50)
    terra2.set_position(terra2.width * 1.5 + 80, janela.height - base_plat.height * 2 - terra1.height)
    terra3.set_position(janela.width - base_plat.width - 50, janela.height - base_plat.height * 2 - terra1.height - 100)
    grama1.set_position(janela.width - base_plat.width - 250, janela.height - base_plat.height * 2 - terra1.height - grama1.height - 50)
    grama2.set_position(grama2.width * 1.5 + 80, janela.height - base_plat.height * 2 - terra1.height - grama2.height)
    grama3.set_position(janela.width - base_plat.width - 50, janela.height - base_plat.height * 2 - terra1.height - 100 - grama2.height)
    player.set_position(0, janela.height - base_plat.height - player.height)
    guarda1.set_position(base_plat.width + plat1.width - 20, janela.height - base_plat.height * 2 - grama1.height - terra1.height - guarda1.height)
    guarda2.set_position(janela.width - base_plat.width + 50, janela.height - base_plat.height * 2 - terra1.height - 100 - grama2.height - guarda2.height)
    guarda3.set_position(janela.width - base_plat.width - 170, janela.height - base_plat.height * 2 - terra1.height - grama1.height - 50 - guarda3.height)
    bandeira.set_position(janela.width - base_grama1.width + 100, janela.height - base_grama1.height - bandeira.height)




    g1 = 0
    g2 = 0
    g3 = 0
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
    lifes = 1

    direita = Sprite("Imagens/player.png")
    esquerda = Sprite("Imagens/-player.png")
    while True:
        fundo.draw()
        if player.collided(grama3) or player.collided(grama2) or player.collided(base_plat) or player.collided(grama1) or player.collided(base_grama1):
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
            guarda2 = Sprite("Imagens/respirar inimigo.png")
            guarda3 = Sprite("Imagens/respirar inimigo.png")
            guarda1.set_position(base_plat.width + plat1.width - 20, janela.height - base_plat.height * 2 - grama1.height - terra1.height - guarda1.height)
            guarda2.set_position(janela.width - base_plat.width + 40, janela.height - base_plat.height * 2 - terra1.height - 100 - grama2.height - guarda2.height)
            guarda3.set_position(janela.width - base_plat.width - 170, janela.height - base_plat.height * 2 - terra1.height - grama1.height - 50 - guarda3.height)
            respirarinimigo = 400
        elif respirarinimigo <= 200:
            guarda1 = Sprite("Imagens/inimigo.png")
            guarda2 = Sprite("Imagens/inimigo.png")
            guarda3 = Sprite("Imagens/inimigo.png")
            guarda1.set_position(base_plat.width + plat1.width - 20, janela.height - base_plat.height * 2 - grama1.height - terra1.height - guarda1.height)
            guarda2.set_position(janela.width - base_plat.width + 40, janela.height - base_plat.height * 2 - terra1.height - 100 - grama2.height - guarda2.height)
            guarda3.set_position(janela.width - base_plat.width - 170, janela.height - base_plat.height * 2 - terra1.height - grama1.height - 50 - guarda3.height)
            respirarinimigo -= 1
        else:
            respirarinimigo -= 1


        if g3 == 0:
            if guarda3.x > player.x and guarda3.x < player.x + guarda3.height:
                if guarda3.collided(player):
                    n_score = luta(janela, 2)
                    if n_score == 0:
                        game_over(janela, score)
                        return 0
                    else:
                        score += n_score
                        g3 = 1

        if g2 == 0:
            if guarda2.x > player.x and guarda2.x < player.x + guarda2.height:
                if guarda2.collided(player):
                    n_score = luta(janela, 3)
                    if n_score == 0:
                        game_over(janela, score)
                        return 0
                    else:
                        score += n_score
                        g2 = 1

        if g1 == 0:
            if guarda1.x > player.x and guarda1.x < player.x + guarda1.height:
                if guarda1.collided(player):
                    n_score = luta(janela, 2)
                    if n_score == 0:
                        game_over(janela, score)
                        return 0
                    else:
                        score += n_score
                        g1 = 1

        if player.x > janela.width:
            doc = open("scores.txt",'a')
            doc.write(("{} {} \n").format(nome,score))
            doc.close()  
            vitoria(janela, score)         #tela de vitoria
          
            return 0

        if player.y > janela.height:
            doc = open("scores.txt",'a')
            doc.write(("{} {} \n").format(nome,score))
            doc.close()
            game_over(janela, score)
            return 0


        # base_plat2.draw()
        # plat1.draw()
        terra1.draw()
        terra2.draw()
        terra3.draw()
        grama1.draw()
        grama2.draw()
        grama3.draw()
        base_plat.draw()
        base_grama1.draw()
        bandeira.draw()
        #base_plat3.draw()

        if g1 == 0:
            guarda1.draw()
        if g2 == 0:
            guarda2.draw()
        if g3 == 0:
            guarda3.draw()
        player.draw()
        janela.update()
