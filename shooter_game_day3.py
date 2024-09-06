#Create your own shooter

from pygame import *

from spriteClass import GameSprite

from random import randint

# Player Class
class Player(GameSprite):
    
    def controller(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(player_image='bullet.png', 
                        player_x=self.rect.centerx, #center of sprite
                        player_y=self.rect.top, #top of sprite
                        size_x=15, 
                        size_y=20,
                        player_speed=3)
        bullet_group.add(bullet)

# Bullet Class
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

# Enemy Class
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

rocket = Player(player_image='rocket.png', 
                player_x=5, 
                player_y=420, 
                size_x=65, 
                size_y=65,
                player_speed=5)

ufo_group = sprite.Group()
for i in range(1, 11):
    ufo = Enemy(player_image='ufo.png', 
                player_x=randint(40, 620), 
                player_y=5, 
                size_x=80, 
                size_y=50,
                player_speed= randint(1, 3) )
    ufo_group.add(ufo)

bullet_group = sprite.Group()

run = False

finish = False

font.init()
style = font.Font(None, 30)

missing = 0

while not run:

    for e in event.get():
        if e.type == QUIT:
            run = True

        # fire
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.fire()

    if not finish:
        window.blit(background, (0,0))

        missed = style.render('Missed: ' + str(missing), 1, (255, 255, 255))
        window.blit(missed, (5,5))

        score = style.render('Scores: ', 1, (255, 255, 255))
        window.blit(score, (5,30))


        rocket.reset(window)
        rocket.controller()
        ufo_group.update()

        bullet_group.update()

        ufo_group.draw(window)

        bullet_group.draw(window)

        display.update()

        time.delay(50) 