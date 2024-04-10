import pygame
import random
import sys

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorWHITE = (255, 255, 255)
colorBLACK = (0, 0, 0)
colorGREEN = (0, 255, 0)

# Sounds
collision_sound = pygame.mixer.Sound("./Resources/crash.wav")
coin_sound = pygame.mixer.Sound("./Resources/coin_sound.wav")
win_sound = pygame.mixer.Sound("./Resources/win_sound.mp3")
achievement_sound = pygame.mixer.Sound("./Resources/achievement.mp3")
pygame.mixer.music.load("./Resources/music.wav")
pygame.mixer.music.play(-1)

BACKGROUND = pygame.image.load("./Resources/AnimatedStreet.png")

clock = pygame.time.Clock()

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1500)

# Speed
ENEMY_SPEED = 4
COIN1_SPEED = 4
COIN2_SPEED = 8
COIN3_SPEED = 15

# Counter
counter = pygame.image.load("./Resources/Counter.png")
new_counter = pygame.transform.scale(counter, (105, 48))

# Fonts
font1 = pygame.font.SysFont('Calibri', 30)
font2 = pygame.font.SysFont('Calibri', 60)

# Classes
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-8, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(8, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, 35)

    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, ENEMY_SPEED)
        else:
            self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

class Coin(pygame.sprite.Sprite):
    def __init__(self, image_path, speed):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed
        
    def move(self):
        if self.rect.bottom < HEIGHT:
            self.rect.move_ip(0, self.speed)
        else:
            self.rect.center = (random.randint(self.rect.width // 2, WIDTH - self.rect.width // 2), 35)

class Coin1(Coin):
    def __init__(self):
        super().__init__("./Resources/Coin.png", COIN1_SPEED)

class Coin2(Coin):
    def __init__(self):
        super().__init__("./Resources/Coin2.png", COIN2_SPEED)

class Coin3(Coin):
    def __init__(self):
        super().__init__("./Resources/Coin3.png", COIN3_SPEED)


SPEED = 5
COINS_COUNT = 0

# Sprite groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Player()
E1 = Enemy()
C1 = Coin1()
C2 = Coin2()
C3 = Coin3()

# Random coin
random_coin = random.choice([C1,C2,C3])
coins.add(random_coin)
all_sprites.add(P1, E1, random_coin)

enemies.add(E1)

done = False

FPS = 60

# Achievement 
show_achievement = False  
achievement_timer = 0
ach_received = False

# Game Logic
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
    
    for coin in coins:
        if pygame.sprite.collide_rect(coin, E1):
            coin.rect.y = -100  
            coin.rect.x = random.randint(0, WIDTH - coin.rect.width) 

        if pygame.sprite.spritecollideany(P1, enemies):
            Game_Over = font2.render('Game Over!', True, colorBLACK)
            screen.fill(colorRED)
            screen.blit(Game_Over, (55, 180))
            text2 = font1.render(f'Total coins collected: {COINS_COUNT}', True, colorBLUE)
            screen.blit(text2, (60, 280))

            pygame.mixer.music.stop()
            achievement_sound.stop()
            collision_sound.play()

            pygame.display.flip()
            pygame.time.delay(2000)
            print("Collision!")
            pygame.quit()
            sys.exit()
    
    # Coins Collision
    coins_collected = pygame.sprite.spritecollideany(P1, coins)

    if coins_collected:
        coin_sound.play()
        coins.remove(random_coin)
        all_sprites.remove(random_coin)
        random_coin = random.choice([C1, C2, C3])
        coins.add(random_coin)
        all_sprites.add(random_coin)
        
        coins_collected.rect.x = -100
        if coins_collected == C1:
            COINS_COUNT += 1
        elif coins_collected == C2:
            COINS_COUNT += 3
        elif coins_collected == C3:
            COINS_COUNT += 5

    if COINS_COUNT >= 25 and COINS_COUNT <= 50:
        ENEMY_SPEED = 8
        
    elif COINS_COUNT >= 50 and COINS_COUNT <= 75:
        ENEMY_SPEED = 12

    elif COINS_COUNT >= 100:
        ENEMY_SPEED = 15
        if event.type == INC_SPEED:
            ENEMY_SPEED += 0.2

    if COINS_COUNT >= 150:
        You_win = font2.render('You win!', True, colorWHITE)

        win_sound.play()
        pygame.mixer.music.stop()
        achievement_sound.stop()

        screen.fill(colorGREEN)
        screen.blit(You_win, (100, 180))
        text2 = font1.render(f'Total coins collected: {COINS_COUNT}', True, colorBLUE)
        screen.blit(text2, (60, 280))
        pygame.display.flip()
        pygame.time.delay(2000)
        print("Collision!")
        pygame.quit()
        sys.exit()

    if COINS_COUNT >= 75 and COINS_COUNT <= 85:
        show_achievement = True
        achievement_sound.play()
        achievement_timer = pygame.time.get_ticks() + 1000 

    if show_achievement:
        ach_line1 = 'Almost a millionaire!'
        ach_line2 = 'Achievement 1 unlocked'
    
        ach_line1 = font1.render(ach_line1, True, colorRED)
        ach_line2 = font1.render(ach_line2, True, colorBLUE)
    
        screen.blit(ach_line1, (75, 140))
        screen.blit(ach_line2, (50, 100))
    
    if show_achievement and pygame.time.get_ticks() >= achievement_timer:
        show_achievement = False
    

    text1 = font1.render(f'{COINS_COUNT}', True, colorWHITE)

    screen.blit(new_counter, (280, 10))
    screen.blit(text1, (340, 20))  
    pygame.display.flip()
    clock.tick(FPS)