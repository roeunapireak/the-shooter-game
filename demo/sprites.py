from pygame import *
from random import randint

# child class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, 
                 player_wight, player_height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_wight, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        self.bullets = sprite.Group()

    def reset(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(GameSprite):
    def update(self):

        keys = key.get_pressed()

        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_RIGHT] and self.rect.x < 700 - 80:
            self.rect.x += self.speed


    def fire(self):
        bullet = Bullet('bullet.png', 
                        self.rect.centerx, self.rect.top,
                        5,  15,20)
        
        self.bullets.add(bullet)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()

