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
pygame.time.set_timer(INC_SPEED, 1000)

ENEMY_SPEED = 4
COIN_SPEED = 4

counter = pygame.image.load("./Resources/Counter.png")
new_counter = pygame.transform.scale(counter, (105, 48))

font1 = pygame.font.SysFont('Calibri', 30)
font2 = pygame.font.SysFont('Calibri', 60)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-7.5, 0)
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(7.5, 0)

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
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./Resources/Coin.png")
        self.rect = self.image.get_rect()
        
    def move(self):
        if self.rect[1] + self.rect[3] < HEIGHT:
            self.rect.move_ip(0, COIN_SPEED)
        else:
            self.rect.center = (random.randint(self.rect[2] // 2, WIDTH - self.rect[2] // 2), 35)

SPEED = 5

COINS_COUNT = 0

enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

P1 = Player()
E1 = Enemy()
C = Coin()

enemies.add(E1)
coins.add(C)
all_sprites.add(P1, E1, C)

done = False

FPS = 60

show_achievement = False  
achievement_timer = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == INC_SPEED:
            ENEMY_SPEED += 0.3
            COIN_SPEED += 0.3

    screen.blit(BACKGROUND, (0, 0))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

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
        
    
    coins_collected = pygame.sprite.spritecollideany(P1, coins)

    if coins_collected:
        coin_sound.play()
        print("Coin collected!")
        coins_collected.rect.x = -100
        COINS_COUNT += 1
    
    if COINS_COUNT == 10:
        achievement_sound.play()
        show_achievement = True
        achievement_timer = pygame.time.get_ticks() + 2000 

    if show_achievement:
        ach1_line1 = 'Almost a millionaire!'
        ach1_line2 = 'Achievement 1 unlocked'
    
        ach1_line1 = font1.render(ach1_line1, True, colorRED)
        ach1_line2 = font1.render(ach1_line2, True, colorBLUE)
    
        screen.blit(ach1_line1, (75, 140))
        screen.blit(ach1_line2, (50, 100))
    
    if show_achievement and pygame.time.get_ticks() >= achievement_timer:
        show_achievement = False
    
    text1 = font1.render(f'{COINS_COUNT}', True, colorWHITE)

    screen.blit(new_counter, (280, 10))
    screen.blit(text1, (340, 20))  
    pygame.display.flip()
    clock.tick(FPS)