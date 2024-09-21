#Create your own shooter

from pygame import *

from spriteClass import Player



window = display.set_mode((700,500))
display.set_caption('Shooter Game')

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

clock = time.Clock()

mixer.init()
mixer.music.load('space.ogg')
# mixer.music.play()

rocket = Player('rocket.png', 5 , 420 , 3)

run = False

while not run:
    window.blit(background, (0,0))

    rocket.reset(window)
    rocket.controller()

    for e in event.get():
        if e.type == QUIT:
            run = True


    clock.tick(60)
    display.update()

