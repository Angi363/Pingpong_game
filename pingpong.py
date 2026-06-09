from pygame import *

window = display.set_mode((700, 500))
clock = time.Clock()
display.set_caption('Ping-pong')

class GameSprite(sprite.Sprite):
    def __init__(self, name_image, height, width, x, y):
        super().__init__()
        self.image = transform.scale(image.load(name_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self, button):
        keys_pressed = key.get_pressed()
        if keys_pressed[button]:
            if keys_pressed[K_UP] and self.rect.y > 0:
                self.rect.y -= 3
            if keys_pressed[K_DOWN] and self.rect.y < 375:
                self.rect.y += 3

class Ball(GameSprite):
    def auto_move(self, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y

font.init()
lose1 = font.Font(None, 50).render('Левая ракетка проиграла', True, (150, 0, 0))
win1 = font.Font(None, 50).render('Правая ракетка победила', True, (0, 200, 0))
lose2 = font.Font(None, 50).render('Правая ракетка проиграла', True, (150, 0, 0))
win2 = font.Font(None, 50).render('Левая ракетка победила', True, (0, 200, 0))
player1 = Player('racket.png', 125, 30, 50, 200)
player2 = Player('racket.png', 125, 30, 615, 200)
ball = Ball('tenis_ball.png', 50, 50, 325, 225)
run = True
finish = False
move_y = 2
move_x = 2
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:
        window.fill((150, 250, 255))
        player1.reset()
        player1.move(K_1)
        player2.reset()
        player2.move(K_2)
        ball.reset()
        ball.auto_move(move_x, move_y)
        if ball.rect.y < 0 or ball.rect.y > 450:
            move_y = -move_y
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            move_x = -move_x
        if ball.rect.x < -60:
            window.blit(lose1, (140, 150))
            window.blit(win1, (130, 250))
            finish = True
        if ball.rect.x > 700:
            window.blit(lose2, (130, 150))
            window.blit(win2, (140, 250))
            finish = True
    display.update()
    clock.tick(60)