import pygame

pygame.init()

# Screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# Program
done = False
x = 400
y = 300
RED = (255, 0, 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x += 20
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_UP]:
        y -= 20
    if keys[pygame.K_DOWN]:
        y += 20
    
    if x >= 800:
        x -= 20
    elif x <= 0:
        x += 20

    if y >= 600:
        y -= 20
    elif y <= 0:
        y += 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, RED, (x, y), 25)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
