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

class GameSprite(sprite.Sprite):

    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (whight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite)
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

racket1 = Player()




while game:
    for e in event.get():
        if e.type == QUIT
            game = False


display.update()
clock.tick(FPS)

