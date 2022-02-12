if delaypulo == 0:
    if teclado.key_pressed("SPACE"):
        for i in range(5):
            player.y -= velplayery * janela.delta_time()
            y -= velplayery * janela.delta_time()
            if movimento <= 0:
                player = Sprite("pular1.png")
                movimento += 1
                player.set_position(x, y)
            elif movimento <= 16:
                player = Sprite("pular2.png")
                movimento += 1
                player.set_position(x, y)
            elif movimento <= 32:
                player = Sprite("pular3.png")
                movimento += 1
                player.set_position(x, y)
            elif movimento <= 48:
                player = Sprite("pular4.png")
                movimento += 1
                player.set_position(x, y)
            elif movimento <= 64:
                player = Sprite("pular5.png")
                movimento = 0
                player.set_position(x, y)
            if player.x < 0:
                player.x = 0
    delaypulo = 500
else:
    delaypulo -= 1