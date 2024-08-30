#Create your own shooter

from pygame import *

from spriteClass import Player, GameSprite

# chill class of GameSprite
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed

        global lost
        if self.rect.y > 500:
            self.rect.x = randint(80, 420)
            self.rect.y = 0

            lost += 1

window = display.set_mode((700,500))
display.set_caption('Shooter Game')

background = transform.scale(image.load('galaxy.jpg'), (700, 500))

# clock = time.Clock()

mixer.init()
mixer.music.load('space.ogg')
# mixer.music.play()

rocket = Player('rocket.png', 5 , 420 , 3)

from random import randint
monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(player_image='ufo.png', 
                    player_x=randint(80, 420), 
                    player_y=-40, 
                    player_speed=5 )
    monsters.add(monster)

font.init()
style = font.Font(None, 36)

run = False
lost = 0

finish = False

while not run:

    for e in event.get():
        if e.type == QUIT:
            run = True

        
    if not finish:
        window.blit(background, (0,0))

        text_lose = style.render("Missed: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10, 20))

        rocket.reset(window)
        rocket.controller()

        monsters.update()

        monsters.draw(window)

        display.update()


    time.delay(50)
    # display.update()

