#Create your own shooter

from pygame import *

from spriteClass import Player, GameSprite

from random import randint

# child class of GameSprite
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed

        global missing

        if self.rect.y > 500:
            self.rect.x = randint(5, 620)
            self.rect.y = 0 

            missing += 1


window = display.set_mode((700,500))
display.set_caption('Shooter Game')

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

clock = time.Clock()

mixer.init()
mixer.music.load('space.ogg')
# mixer.music.play()

rocket = Player('rocket.png', 5 , 420 , 5)

ufo_group = sprite.Group()
for i in range(1, 11):
    ufo = Enemy(player_image='ufo.png', 
                player_x=randint(40, 620), 
                player_y= 5, 
                player_speed= randint(1, 3) )
    ufo_group.add(ufo)


run = False

finish = False

font.init()
style = font.Font(None, 30)

missing = 0

while not run:

    for e in event.get():
        if e.type == QUIT:
            run = True

    if not finish:
        window.blit(background, (0,0))

        missed = style.render('Missed: ' + str(missing), 1, (255, 255, 255))
        window.blit(missed, (5,5))

        score = style.render('Scores: ', 1, (255, 255, 255))
        window.blit(score, (5,30))


        rocket.reset(window)
        rocket.controller()

        ufo_group.update()

        ufo_group.draw(window)

        display.update()

        time.delay(50) 