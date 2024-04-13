import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

pygame.display.set_caption("HALL KILLER ")
icon = pygame.image.load("robot.png")
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load("maratha.png")
x1 = 370
y1 = 480
xchange = 0
ychange = 0

# enemy
enemyimg1 = pygame.image.load("aryans.png")
enemyimg2 = pygame.image.load("nawabs.png")
enemyimg3 = pygame.image.load("ksytariyas.png")
enemyimg4 = pygame.image.load("shauryas.png")
enemyimg=[enemyimg1,enemyimg2,enemyimg3,enemyimg4]
enemies = []
enemy_speed = 0.075

# bullet
bulletimg = pygame.image.load("cigarette-butt.png")
bullets = []
bullet_speed = 0.3
# SCORE
score=0
font =pygame.font.Font("freesansbold.ttf",32)
score_x=10
score_y=10
player_state="ALIVE"
def show_score(x,y,score_number):
    score=font.render("SCORE :"+str(score_number),True,(255,255,255))
    screen.blit(score,(x,y))

def collision(enemyx, enemyy, bulletx, bullety):
    distance = (pow((enemyx - bulletx), 2) + pow((enemyy - bullety), 2))
    distance = pow(distance, 0.5)
    # print(distance)
    if distance >= 0 and distance <= 30:
        return True
    else:
        return False
def gameover(score):
    over=font.render("JAI SHIVAJI ",True,(255,255,255))
    screen.blit(over,(300,300))
    final=font.render("Final Score : "+str(score),True,(255,255,255))
    screen.blit(final,(250,100))


def fire_bullet(x, y):
    bullets.append({'x': x, 'y': y})

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y,c):
    
    screen.blit(enemyimg[c], (x, y))

background = pygame.image.load("astronomy-1867616_1280.jpg")
spawn_timer = 0
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -0.4
            elif event.key == pygame.K_RIGHT:
                xchange = 0.4
            elif event.key == pygame.K_UP:
                ychange = -0.4
            elif event.key == pygame.K_DOWN:
                ychange = 0.4
            elif event.key == pygame.K_SPACE:
                fire_bullet(x1, y1)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xchange = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                ychange = 0
    if player_state=="ALIVE":
        if (x1 + xchange) < 736 and (x1 + xchange) > 0:
            x1 += xchange
        if (y1 + ychange) < 536 and (y1 + ychange) > 0:
            y1 += ychange

        if len(enemies) < 3:  
            if spawn_timer <= 0:
                enemyx = random.randint(0, 736)
                enemyy = random.randint(10,50 )
                enemies.append({'x': enemyx, 'y': enemyy,'id':random.randint(0,3)})
                spawn_timer = 50
            else:
                spawn_timer -= 1
        
        for enemy_pos in enemies:
            enemy_pos['y'] += enemy_speed
            enemy(enemy_pos['x'], enemy_pos['y'],enemy_pos['id'])
            if (collision(enemy_pos['x'], enemy_pos['y'],x1,y1)==True):
                    
                    player_state="DEATH"
        

        for bullet in bullets:
            bullet['y'] -= bullet_speed
            if bullet['y'] < 0:
                bullets.remove(bullet)
                score=score-1
            else:
                screen.blit(bulletimg, (bullet['x'] + 16, bullet['y'] + 10))

        for bullet in bullets:
            for enemy_pos in enemies:
                
                if collision(enemy_pos['x'], enemy_pos['y'], bullet['x'], bullet['y']):
                    bullets.remove(bullet)
                    enemies.remove(enemy_pos)
                    score=score+5
                if enemy_pos["y"] > 536:
                    enemies.remove(enemy_pos) 
                    score =score-2 
                    
                


                    
        show_score(score_x,score_y,score)
        player(x1, y1)
    
    else:
        gameover(score)
    
        
    pygame.display.update()
