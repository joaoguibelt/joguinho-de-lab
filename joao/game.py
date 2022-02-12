from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from PPlay.gameobject import *
def gamei(pontuacao):
    janela = Window(800, 450)
    janela.set_title("space invaders")
    fundo = GameImage("estrelas 8bit.jpg")
    tiro = []
    fps = 0
    contador = 0
    delaybala = 0
    delaybalainimigo = 50
    tempotempo = 0
    balainimigo = Sprite("bala alien.png")
    tiroinimigo = []
    vida = Sprite("vidas.png")
    quantvida = 3
    mouse = Window.get_mouse()
    #pontuacao = 0
    delayalienzao = 1000
    teclado = Window.get_keyboard()
    velnavex = 200
    kill = 0
    velbalay = 400
    velalienx = 100
    alienzaoo = Sprite("alienzao.png")
    alienzao = []
    velalienzaox = 250
    bala = Sprite("bala.png")
   # if gamemode == 0:
     #   velnavex = 300
    #if gamemode == 2:
      #  velnavex = 10
    quantinimigo = 0
    nave = Sprite("nave.png")
    nave.set_position(janela.width / 2, janela.height - nave.height)
    vida.set_position(0, 0)
    maisalien = 0
    aliens = []
    for i in range(3):
        aliens.append([])
        for j in range(3):
            alien = Sprite("alien.png")
            aliens[i].append(alien)
            alien.set_position(janela.width/2 + i * 50, 0 + j * 30)
    descer = 0
    reset = 1
    contadorinimigo = 0
    while True:
        if delayalienzao > 0:
            delayalienzao -= 1
        fundo.draw()
        if delaybala == 0:
            if teclado.key_pressed("SPACE"):
                bala = Sprite("bala.png")
                bala.set_position(nave.x + nave.width / 2, janela.height - nave.height - bala.height)
                tiro.append(bala)
                delaybala = 100
        else:
            delaybala -= 1
        for i in range(len(aliens)):
            for j in range(len(aliens[i])):
                try:
                    alien = aliens[i][j]
                    alien.draw()
                    alien.x += velalienx * janela.delta_time()
                    if alien.x > janela.width - alien.width or alien.x < 0:
                        velalienx *= -1
                        descer = 1
                    if alien.y >= janela.height - alien.height:
                        #gameovere(pontuacao)
                        return pontuacao
                except:
                    pass
        for i in range(len(aliens)):
            for j in range(len(aliens[i])):
                try:
                    if delaybalainimigo == 0:
                        balainimigo = Sprite("bala alien.png")
                        balainimigo.set_position(aliens[i][j].x, aliens[i][j].y + balainimigo.height)
                        tiroinimigo.append(balainimigo)
                        delaybalainimigo = 5000
                except:
                    pass
                delaybalainimigo -= 1
        for k in range(len(tiroinimigo)):
            tiroinimigo[k].y += velbalay * janela.delta_time()
        for i in range(len(tiroinimigo)):
            tiroinimigo[i].draw()
            if tiroinimigo[i].y >= janela.height:
                tiroinimigo.pop(i)
                break
        for i in range(len(tiroinimigo)):
            if tiroinimigo[i].collided(nave):
                quantvida -= 1
                tiroinimigo.pop(i)
                break
        hit = 0
        erro = 0
        for z in range(len(tiro) - erro):
            z -= erro
            for i in range(len(aliens)):
                try:
                    for v in range(len(aliens) - 1, -1, -1):
                        for j in range(len(aliens[v]) - 1, -1, -1):
                            if tiro[z].collided(aliens[i][j]):
                                tiro.pop(z)
                                aliens[v].pop(j)
                                kill += 1
                                pontuacao += 100
                                erro += 1
                                hit = 1
                                break
                            elif tiro[z].collided(alienzao[0]):
                                tiro.pop(z)
                                pontuacao += 500
                                alienzao.pop(0)
                                hit = 1
                                delayalienzao = 1500
                                break
                        if hit == 1:
                            break
                    if hit == 1:
                        break
                except:
                    pass


        if delayalienzao == 0:
            if len(alienzao) == 0:
               alienzaoo.set_position(0, 0)
               alienzao.append(alienzaoo)
            alienzao[0].x += velalienzaox * janela.delta_time()
        for i in range(len(aliens)):
            for j in range(len(aliens[i])):
                try:
                    alien = aliens[i][j]
                    if descer == 1:
                        alien.y += janela.height / 16
                except:
                    pass
        descer = 0
        if nave.x < 0:
            nave.x = 0
        if nave.x > janela.width - nave.width:
            nave.x = janela.width - nave.width
        if teclado.key_pressed("D"):
            nave.x += velnavex * janela.delta_time()
        if teclado.key_pressed("A"):
            nave.x -= velnavex * janela.delta_time()
        if teclado.key_pressed("esc"):
            return 1
        try:
            if alienzao[0].x >= janela.width:
                delayalienzao = 1500
                alienzao.pop(0)
        except:
            pass
        tempotempo += janela.delta_time()
        contador += 1
        if tempotempo >= 1:
            fps = contador
            contador = 0
            tempotempo = 0
        for i in range(len(tiro)):
            tiro[i].y -= velbalay * janela.delta_time()
        for i in range(len(tiro)):
            tiro[i].draw()
            if tiro[i].y < 0:
                tiro.pop(i)
                break
        if quantvida == 0:
            #ranking = open('pontuaçoes.txt', 'r+')
            #ranking.write(str(pontuacao))
            #ranking.close()
            #gameovere(pontuacao)
            return pontuacao
        for i in range(len(aliens)):
            for j in range(len(aliens[i])):
                try:
                    if nave.collided(aliens[i][j]):
                        #gameovere(pontuacao)

                        return pontuacao
                except:
                    pass
        if reset == 1:
            if contadorinimigo == 0:
                for i in range(len(aliens)):
                    for j in range(len(aliens[i])):
                        quantinimigo += 1
            contadorinimigo = 1
        if kill == quantinimigo:
            maisalien += 1
            kill = 0
            quantinimigo = 0
            for i in range(3 + maisalien):
                aliens.append([])
                for j in range(3):
                    alien = Sprite("alien.png")
                    aliens[i].append(alien)
                    velalienx += 20
                    alien.set_position(janela.width / 2 + i * 50, 0 + j * 30)
            reset = 1
            contadorinimigo = 0
        vida.draw()
        janela.draw_text(str(quantvida), vida.width + 12, 0, 25, (255, 255, 255), "arial", False, False)
        janela.draw_text(str(pontuacao), janela.width/2, 0, 25, (255, 255, 255), "arial", False, False)
        janela.draw_text(str(fps), janela.width - 35, 0, 25, (255, 255, 255), "arial", False, False)
        nave.draw()
        try:
           alienzao[0].draw()
        except:
            pass
        janela.update()

