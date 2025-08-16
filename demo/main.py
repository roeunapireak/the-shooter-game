
from pygame import *
from sprites import GameSprite, Player
from random import randint

lost = 0 
score = 0 
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.x = randint(65, 700-65)
            self.rect.y = 0 

            lost += 1

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter Game")
background = transform.scale(image.load("galaxy.jpg"), 
                             (win_width, win_height))


clock = time.Clock()

''' sprites '''
player = Player(player_image='rocket.png', 
                    player_x=(700/2)-60,
                    player_y=500-70, 
                    player_speed=5, 
                    player_wight=65, player_height=65)



monsters = sprite.Group()
for i in range(5):
    monster = Enemy(player_image='ufo.png', 
                        player_x=randint(65, 700-65),
                        player_y=0, 
                        player_speed=randint(1,3), 
                        player_wight=65, player_height=65)
    monsters.add(monster)

asteroids = sprite.Group()
for i in range(3):
    asteroid = Enemy(player_image='asteroid.png', 
                        player_x=randint(65, 700-65),
                        player_y=0, 
                        player_speed=randint(1,3), 
                        player_wight=65, player_height=65)
    asteroids.add(asteroid)

font.init()
style = font.Font(None, 20)
style2 = font.Font(None, 60)


game = False

finish = True

# Application
while not game:

    for e in event.get():
        if e.type == QUIT:
           game = True

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    

    # Game sense
    if finish:

        window.blit(background, (0,0))
        player.reset(window)
        player.update()

   
        monsters.draw(window)
        monsters.update()

        asteroids.draw(window)
        asteroids.update()

        player.bullets.draw(window)
        player.bullets.update()

        text_missing = style.render("Missed: "+str(lost), 1, (255, 255, 255))
        window.blit(text_missing, (10,20))

        text_score = style.render("Scores: "+str(score), 1, (255, 255, 255))
        window.blit(text_score, (10,50))

        collide = sprite.groupcollide(monsters, player.bullets, True, True) 

        for i in collide:
            monster = Enemy(player_image='ufo.png', 
                    player_x=randint(65, 700-65),
                    player_y=0, 
                    player_speed=randint(1,3), 
                    player_wight=65, player_height=65)
            monsters.add(monster)
            score += 1 


        # lose condition
        if lost >= 20 or sprite.spritecollide(player, monsters, False) or sprite.spritecollide(player, asteroids, False):
            lose = style2.render('YOU LOSE!', True, (255, 255, 255))
            window.blit(lose, (270,200))
            finish = False

        # win condition
        if score >= 5: 
            win = style2.render('VICTORY !!!', True, (255, 255, 255))
            window.blit(win, (270,200))
            finish = False
            
        display.update()


    else:  # replay the game sense 
        
        lost = 0
        score = 0 
        
        for m in monsters:
            m.kill()
        for a in asteroids:
            a.kill()
        for b in player.bullets:
            b.kill()

        for i in range(5):
            monster = Enemy(player_image='ufo.png', 
                                player_x=randint(65, 700-65),
                                player_y=0, 
                                player_speed=randint(1,3), 
                                player_wight=65, player_height=65)
            monsters.add(monster)
        
        for i in range(3):
            asteroid = Enemy(player_image='asteroid.png', 
                                player_x=randint(65, 700-65),
                                player_y=0, 
                                player_speed=randint(1,3), 
                                player_wight=65, player_height=65)
            asteroids.add(asteroid)

        time.delay(6000) # milliseconds
        finish = True    


    time.delay(35) 




