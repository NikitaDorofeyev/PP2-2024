import pygame
from datetime import datetime

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

done = False

#Clock
main_clock = pygame.image.load('mainclock.png')
mickey_clock = pygame.transform.scale(main_clock, (800, 600))

# Left arm
left_arm = pygame.image.load('leftarm.png')
new_left_arm = pygame.transform.scale(left_arm, (35, 583.33))

# Right arm
right_arm = pygame.image.load('rightarm.png')
scaled_right_arm = pygame.transform.scale(right_arm, (800, 600))
new_right_arm = pygame.transform.rotate(scaled_right_arm, -20)

clock_center = (400, 300)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))


    # Angles
    current_time = datetime.now()
    second_angle = (current_time.second / 60) * 360 
    minute_angle = (current_time.minute / 60) * 360


    # Left
    rotated_left = pygame.transform.rotate(new_left_arm, -second_angle)

    # Right
    rotated_right = pygame.transform.rotate(new_right_arm, -minute_angle)

    # Arms positions
    left_arm_rect = rotated_left.get_rect(center=clock_center)
    right_arm_rect = rotated_right.get_rect(center=clock_center)

    screen.blit(mickey_clock, (0, 0))
    screen.blit(rotated_left, left_arm_rect)
    screen.blit(rotated_right, right_arm_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()   