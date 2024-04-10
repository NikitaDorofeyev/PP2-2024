import pygame
import random
from color_palette import *
from collections import namedtuple

pygame.init()

# Fonts 
font = pygame.font.SysFont("Vergena", 30, True)
bigfont = pygame.font.SysFont("Vergena", 50, True)

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
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Snake')

        # Starting positions, directions 
        self.direction = Direction.RIGHT
        self.head = Point(self.WIDTH // 2, self.HEIGHT // 2)
        # The initial snake with a length of 3 with its body coordinates 
        self.snake = [self.head,
                      Point(self.head.x - CELL, self.head.y),
                      Point(self.head.x - (2 * CELL), self.head.y)]
        self.level = 0
        self.score = 0
        self.food = None
        self.food_move()
        
    # Moving Food to random positions 
    def food_move(self):
        x = random.randint(0, (self.WIDTH - CELL) // CELL) * CELL
        y = random.randint(0, (self.HEIGHT - CELL) // CELL) * CELL
        self.food = Point(x, y)
        if self.food in self.snake:
            self.food_move()
            
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
            if self.score//5 > self.level:
                global SPEED
                self.level = self.score//5
                SPEED += 3
        else:
            self.snake.pop()

        # Update Interface

        self.update()
        self.clock.tick(SPEED)

    def collision(self):
        # Hits Boundary 
        if self.head.x > self.WIDTH - CELL or self.head.x < 0 or self.head.y > self.HEIGHT - CELL or self.head.y < 0:
            pygame.display.flip()
            return True
        # Hits Itself 
        global game_over
        if self.head in self.snake[1:]:
            pygame.display.flip()
            return True

        return False

    def update(self):
        self.screen.fill((colorGREEN))

        for skin in self.snake:
            pygame.draw.rect(self.screen,  (colorBLACK), pygame.Rect(skin.x, skin.y, CELL, CELL))
            pygame.draw.rect(self.screen, (colorYELLOW), pygame.Rect(skin.x + 4, skin.y + 4, 12, 12))

        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.x, self.food.y, CELL, CELL))

        text1 = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text2 = font.render(f"Level: {self.level}", True, (255, 255, 255))
        self.screen.blit(text1, (10, 10))
        self.screen.blit(text2, (10, 30))
        if self.collision():
            text3 = bigfont.render(f"Press R to Restart", True, (255, 255, 255))
            self.screen.blit(text3, (self.HEIGHT // 2 - 50, self.WIDTH // 2 - 140))
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
                        SPEED = 7
                        game = Game()
                        game_over = False

pygame.quit()
exit()
