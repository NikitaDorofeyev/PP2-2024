import pygame
import random
import time
from color_palette import *
from collections import namedtuple

pygame.init()

# Fonts 
font = pygame.font.SysFont("Roboto-Bold .ttf", 30, True)
bigfont = pygame.font.SysFont("Roboto-Bold .ttf", 50, True)

# Directions 
class Direction():
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    UP = 'UP'
    DOWN = 'DOWN'

# Getting Positions 
Point = namedtuple('Point', 'x y')

# Variables 
CELL = 20
SPEED = 7
running = True
game_over = False

# Main Class 
class Game:
    def __init__(self, WIDTH=800, HEIGHT=600):
        # Initializing 
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Snake')

        # Starting positions, directions 
        self.direction = Direction.RIGHT
        self.head = Point(self.WIDTH // 2, self.HEIGHT // 2)

        # The initial snake with a length of 3 with its body coordinates 
        self.snake = [self.head,
                      Point(self.head.x - CELL, self.head.y),
                      Point(self.head.x - (2 * CELL), self.head.y)]
        
        self.megafood_exists = False # Appearance of Megafood
        self.level = 0 # Level
        self.score = 0
        self.food = None
        self.megafood = None
        self.current = 0 # Current time
        self.start = 0 # Start time
        self.difference = 0 # difference between times
        self.counter = 10 # Time
        self.food_move()

    # Moving Food to random positions 
    def food_move(self):
        x = random.randint(0, (self.WIDTH - CELL) // CELL) * CELL
        y = random.randint(0, (self.HEIGHT - CELL) // CELL) * CELL
        self.food = Point(x, y)
        if self.food in self.snake:
            self.food_move()

    # Moving Megafood to random positions 
    def megafood_move(self):
        x = random.randint(0, (self.WIDTH - CELL*2) // CELL) * CELL
        y = random.randint(0, (self.HEIGHT - CELL*2) // CELL) * CELL
        self.start = time.time()
        self.megafood = Point(x, y)
        if self.food in self.snake:
            self.megafood_move()

    # Snake Turns and the Exit Condition 
    def play_step(self):
        # User Inputs From Keyboard 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN

        # Move 
        self.move(self.direction)  # Update The Head
        self.snake.insert(0, self.head)

        # Check If Game Over 
        if self.collision():
            global game_over
            game_over = True

        # Place New Food 
        if self.head == self.food:
            self.score += 1
            self.food_move()
            if self.score // 5 > self.level:
                global SPEED
                if random.randint(1, 2) == 1 and not self.megafood:
                    self.megafood_exists = True
                    self.megafood_move()
                SPEED += 3
                self.level = (SPEED-7)//3
        else:
            self.snake.pop()

        if self.head == self.megafood:
            self.score += 5
            self.megafood_exists = False

        # Update Interface 

        self.update()
        self.clock.tick(SPEED)

    def collision(self):
        # Hits Boundary 
        if self.head.x > self.WIDTH - CELL or self.head.x < 0 or self.head.y > self.HEIGHT - CELL or self.head.y < 0:
            pygame.display.flip()
            return True
        # Hits Itself 
        if self.head in self.snake[1:]:
            return True
        return False

    def update(self):
        self.display.fill(colorGREEN1)
        # Drawing Skin of Snake as two different rectangles 
        for skin in self.snake:
            pygame.draw.rect(self.display, colorGREEN2, pygame.Rect(skin.x, skin.y, CELL, CELL))
            pygame.draw.rect(self.display, colorYELLOW, pygame.Rect(skin.x + 4, skin.y + 4, 12, 12))

        # Drawing food 
        pygame.draw.rect(self.display, colorRED, pygame.Rect(self.food.x, self.food.y, CELL, CELL))

        # Drawing Megafood in case of it exists
        if self.megafood_exists:
            pygame.draw.rect(self.display, colorBLACK,
            pygame.Rect(self.megafood.x, self.megafood.y, CELL, CELL))
            pygame.draw.rect(self.display, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            pygame.Rect(self.megafood.x + 4, self.megafood.y + 4, 12, 12))
            
        # Updating Score and Level Text 
        text1 = font.render(f"Score: {self.score}", True, colorWHITE)
        text2 = font.render(f"Level: {self.level}", True, colorWHITE)

        # Updating Timer 
        self.current = time.time()
        self.difference = abs(int(self.current - self.start - self.counter))
        if self.start + self.counter - self.current >= 0:
            text4 = font.render(str(self.difference), True, colorWHITE)

        # Blit Score and Level 
        self.display.blit(text1, (10, 10))
        self.display.blit(text2, (10, 30))
        # Blit Timer if Megafood exists and Time is greater than 0 
        if self.megafood_exists and self.start + self.counter - self.current >= 0:
            self.display.blit(text4, (10, 50))
        else:
            self.megafood_exists = False
        # Blit Restart Text in case of loss 
        if self.collision():
            pygame.mixer.music.stop()
            text3 = bigfont.render(f"Press R to Restart", True, colorWHITE)
            self.display.blit(text3, (self.HEIGHT // 2 - 50, self.WIDTH // 2 - 140))
        pygame.display.flip()

    # Snake Movement 
    def move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += CELL
        elif direction == Direction.LEFT:
            x -= CELL
        elif direction == Direction.DOWN:
            y += CELL
        elif direction == Direction.UP:
            y -= CELL
        self.head = Point(x, y)


# Game Loop 
game = Game()
while running:
    # game_over
    score = game.play_step()
    if game_over == True:
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Restart Conditions 
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        SPEED = 8
                        game = Game()
                        game_over = False


pygame.quit()
exit()