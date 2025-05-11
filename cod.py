from pygame import *

#окно
window = display.set_mode((600, 500))
display.set_caption ("Пинг-Понг")
back = (200, 255, 255)#цвет фона(background)
window.fill(back)
clock = time.Clock()

#важные переменные
Flag = True
game = False

#игровой цикл
while Flag:
    for e in event.get():
        if e.type == QUIT:
            Flag = False

    display.update()
    clock.tick(60)
