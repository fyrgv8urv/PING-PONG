from pygame import *
from random import *

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, speed, x, y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<400:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y<400:
            self.rect.y += self.speed
#окно
window = display.set_mode((600, 500))
display.set_caption ("Пинг-Понг")
back = (200, 255, 255)#цвет фона(background)

clock = time.Clock()

#флаги-состояния игры
Flag = True
game = False
#движение мяча

speed_x = randint(1,2)  
if speed_x == 1:
    speed_x = 3
else:
    speed_x = -3
speed_y = randint(1,2)
if speed_y == 1:
    speed_y = 3
else:
    speed_y = -3
#спрайты ракеток и мяча
racket1 = Player('платформа.png', 5, 30, 150, 50, 100)
racket2 = Player('платформа2.png', 5, 500, 150 , 50, 100)
ball = GameSprite('мяч для пинг понга.png', 3, 280, 230, 50, 50)
#игровой цикл
while Flag:
    for e in event.get():
        if e.type == QUIT:
            Flag = False
    if game!=True:
        racket1.update_l()
        window.fill(back)
        racket2.update_r()
        ball.rect.x+=speed_x
        ball.rect.y+=speed_y

        if ball.rect.y<0 or ball.rect.y>450:
            speed_y*=-1.1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x*=-1




    racket1.reset()
    racket2.reset()
    ball.reset()
    display.update()
    clock.tick(60)
