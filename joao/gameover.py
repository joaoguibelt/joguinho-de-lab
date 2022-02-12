from PPlay.window import *
from PPlay.gameimage import *
def gameovere(pontuacao):
    janela = Window(800, 450)
    janela.set_title("space invaders")
    fundo = GameImage("estrelas 8bit.jpg")
    ponto = []
    teclado = Window.get_keyboard()
    nome = []
    delaynome = 100
    while True:
        fundo.draw()



        janela.draw_text(str("Nome: "), janela.width / 4, janela.height / 1.8, 25, (112, 154, 235), "arial", False, False)
        if len(nome) < 3:
            if delaynome == 0:
                if teclado.key_pressed("Q"):
                    nome.append("Q")
                    delaynome = 50
                if teclado.key_pressed("W"):
                    nome.append("W")
                    delaynome = 50
                if teclado.key_pressed("E"):
                    nome.append("E")
                    delaynome = 50
                if teclado.key_pressed("R"):
                    nome.append("R")
                    delaynome = 50
                if teclado.key_pressed("T"):
                    nome.append("T")
                    delaynome = 50
                if teclado.key_pressed("Y"):
                    nome.append("Y")
                    delaynome = 50
                if teclado.key_pressed("U"):
                    nome.append("U")
                    delaynome = 50
                if teclado.key_pressed("I"):
                    nome.append("I")
                    delaynome = 50
                if teclado.key_pressed("O"):
                    nome.append("O")
                    delaynome = 50
                if teclado.key_pressed("P"):
                    nome.append("P")
                    delaynome = 50
                if teclado.key_pressed("A"):
                    nome.append("A")
                    delaynome = 50
                if teclado.key_pressed("S"):
                    nome.append("S")
                    delaynome = 50
                if teclado.key_pressed("D"):
                    nome.append("D")
                    delaynome = 50
                if teclado.key_pressed("F"):
                    nome.append("F")
                    delaynome = 50
                if teclado.key_pressed("G"):
                    nome.append("G")
                    delaynome = 50
                if teclado.key_pressed("H"):
                    nome.append("H")
                    delaynome = 50
                if teclado.key_pressed("J"):
                    nome.append("J")
                    delaynome = 50
                if teclado.key_pressed("K"):
                    nome.append("K")
                    delaynome = 50
                if teclado.key_pressed("L"):
                    nome.append("L")
                    delaynome = 50
                if teclado.key_pressed("Z"):
                    nome.append("Z")
                    delaynome = 50
                if teclado.key_pressed("X"):
                    nome.append("X")
                    delaynome = 50
                if teclado.key_pressed("C"):
                    nome.append("C")
                    delaynome = 50
                if teclado.key_pressed("V"):
                    nome.append("V")
                    delaynome = 50
                if teclado.key_pressed("B"):
                    nome.append("B")
                    delaynome = 50
                if teclado.key_pressed("N"):
                    nome.append("N")
                    delaynome = 50
                if teclado.key_pressed("M"):
                    nome.append("M")
                    delaynome = 50
            else:
                delaynome -= 1
        if delaynome == 0:
            if teclado.key_pressed("0"):
               try:
                   nome.pop()
                   delaynome = 50
               except:
                 pass
        else:
            delaynome -= 1



        if teclado.key_pressed("ENTER"):
            ranking = open('pontuaçoes.txt', 'a')
            ranking.write(str(nome))
            ranking.write(" - ")
            ranking.write(str(pontuacao))
            ranking.write(" pts\n")
            ranking.close()
            return None
        janela.draw_text(str(nome), janela.width / 4 + 60, janela.height / 1.8, 25, (112, 154, 235), "arial", False, False)
        janela.draw_text(str(pontuacao), janela.width / 3 + 35, janela.height / 2, 25, (125, 5, 45), "arial", False, False)
        janela.draw_text(str("Game Over"), janela.width / 4, janela.height / 4, 100, (25, 55, 245), "arial", False, True)
        janela.draw_text(str("Pontuaçao: "), janela.width / 4, janela.height / 2, 25, (125, 5, 45), "arial", False, False)
        janela.update()