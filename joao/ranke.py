from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
def rankee():
    janela = Window(800, 450)
    janela.set_title("space invaders")
    fundo = GameImage("estrelas 8bit.jpg")
    mouse = Window.get_mouse()
    teclado = Window.get_keyboard()
    ranking = open('pontuaçoes.txt', 'r')
    clone = []
    contador = 0
    while True:
        testando = ranking.readline()
        if len(testando) == 0:
            break
        contador += 1
    ranking.seek(0)
    for i in range(contador):
        testando = ranking.readline()
        testando.split(" ")
        if testando[21] != " ":
            seila = int(testando[18]) + int(testando[19]) * 10 + int(testando[20]) * 100 + int(testando[21]) * 1000
        else:
            seila = int(testando[18]) + int(testando[19]) * 10 + int(testando[20]) * 100
        clone.append(seila)
    ranking.seek(0)
    linhas = ranking.readlines()
    for i in range(len(clone) - 1):
        for j in range(i + 1, len(clone)):
            if clone[i] < clone[j]:
                ajudante = clone[j]
                ajudantelinhas = linhas[j]
                clone[j] = clone[i]
                linhas[j] = linhas[i]
                clone[i] = ajudante
                linhas[i] = ajudantelinhas
    while True:
        fundo.draw()
        janela.draw_text(str("1- "), janela.width / 4, janela.height / 25, 25, (253, 155, 45), "arial", False, True)
        janela.draw_text(str("2- "), janela.width / 4, janela.height / 25 + 40, 20, (25, 155, 35), "arial", False, True)
        janela.draw_text(str("3- "), janela.width / 4, janela.height / 25 + 80, 20, (25, 125, 35), "arial", False, True)
        y = 0
        for i in range(len(clone)):
            janela.draw_text(str(linhas[i]), janela.width / 4 + 40, janela.height / 25 + y, 25, (25, 215, 85), "arial", False, True)
            y += 40
        if teclado.key_pressed("esc"):
            return None
        janela.update()
