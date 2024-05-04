from pygame import*

B
back = (200,255,255)
win_widht = 600
win_height = 500
window = dispay.set_mode((win_widht, win_height))
window.fill(back)

game = True
finish =False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT
            game = False

display.update()
clock.tick(FPS)


