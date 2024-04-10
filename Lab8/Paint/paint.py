import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
current_color = (0, 0, 0)

colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorGREY = (128, 128, 128)
colorGREEN = (0, 255, 0)
colorRED = (255, 0, 0)
colorBLUE = (0, 0, 255)
colorPURPLE = (128, 0 ,128)

# Modes
MODE_LINE = 0
MODE_RECTANGLE = 1
MODE_CIRCLE = 2
MODE_ERASER = 3

current_mode = MODE_LINE

THICKNESS = 5
LMBpressed = False

currX = 0
currY = 0

prevX = 0
prevY = 0

# Layers
line_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
rectangle_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
circle_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
eraser_layer = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA) 

# Function to draw
def draw_line(currX, currY, prevX, prevY, THICKNESS):
    pygame.draw.line(line_layer, current_color, (prevX, prevY), (currX, currY), THICKNESS)

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_rectangle(x1, y1, x2, y2, THICKNESS):
    pygame.draw.rect(rectangle_layer, current_color, calculate_rect(x1, y1, x2, y2), THICKNESS)

def draw_circle(x, y, radius, THICKNESS):
    pygame.draw.circle(circle_layer, current_color, (x, y), radius, THICKNESS)

def draw_eraser(x, y, THICKNESS):
    eraser_layer.fill((0, 0, 0, 0)) # Clear the eraser layer
    radius = THICKNESS // 2  
    border_radius = radius + 2 
    pygame.draw.circle(eraser_layer, colorGREY, (x, y), border_radius)
    pygame.draw.circle(eraser_layer, colorWHITE, (x, y), radius)

    # Erase content from other drawing layers within the eraser circle
    erase_rect = pygame.Rect(x - radius, y - radius, THICKNESS, THICKNESS)
    line_layer.fill((0, 0, 0, 0), erase_rect)
    rectangle_layer.fill((0, 0, 0, 0), erase_rect)
    circle_layer.fill((0, 0, 0, 0), erase_rect)

def clear_eraser_layer():
    eraser_layer.fill((0, 0, 0, 0))

done = False
screen.fill(colorWHITE)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                print("Drawing Type: Rectangle")
                current_mode = MODE_RECTANGLE
                LMBpressed = False
                clear_eraser_layer()

            elif event.key == pygame.K_1:
                print("Drawing Type: Line")
                current_mode = MODE_LINE
                LMBpressed = False
                clear_eraser_layer()

            elif event.key == pygame.K_3:
                print("Drawing Type: Circle")
                current_mode = MODE_CIRCLE
                LMBpressed = False
                clear_eraser_layer()

            elif event.key == pygame.K_e:
                print("Drawing Type: Eraser")
                current_mode = MODE_ERASER
                LMBpressed = False

            # Change thickness regardless of the drawing mode
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS = max(1, THICKNESS - 1)

            # Change color
            if event.key == pygame.K_r:
                current_color = colorRED
            elif event.key == pygame.K_g:
                current_color = colorGREEN
            elif event.key == pygame.K_b:
                current_color = colorBLUE
            elif event.key == pygame.K_BACKSPACE:
                current_color = colorBLACK
            elif event.key == pygame.K_p:
                current_color = colorPURPLE


        # Draw the Line
        if current_mode == MODE_LINE:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("LMB pressed!")
                LMBpressed = True
                currX = event.pos[0]
                currY = event.pos[1]
                prevX = event.pos[0]
                prevY = event.pos[1]

            if event.type == pygame.MOUSEMOTION:
                print("Position of the mouse:", event.pos)
                if LMBpressed:
                    currX = event.pos[0]
                    currY = event.pos[1]
                    draw_line(currX, currY, prevX, prevY, THICKNESS)
                    prevX = currX
                    prevY = currY

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("LMB released!")
                LMBpressed = False

        # Draw the Rectangle
        if current_mode == MODE_RECTANGLE:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("LMB pressed!")
                LMBpressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]

            if event.type == pygame.MOUSEMOTION:
                print("Position of the mouse:", event.pos)
                if LMBpressed:
                    currX = event.pos[0]
                    currY = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("LMB released!")
                LMBpressed = False
                draw_rectangle(prevX, prevY, currX, currY, THICKNESS)
        
        # Draw the Circle
        if current_mode == MODE_CIRCLE:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("LMB pressed!")
                LMBpressed = True
                prevX = event.pos[0]
                prevY = event.pos[1]

            if event.type == pygame.MOUSEMOTION:
                print("Position of the mouse:", event.pos)
                if LMBpressed:
                    currX = event.pos[0]
                    currY = event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("LMB released!")
                LMBpressed = False
                radius = int(((currX - prevX) ** 2 + (currY - prevY) ** 2) ** 0.5)
                draw_circle(prevX, prevY, radius, THICKNESS)

        # Eraser
        if current_mode == MODE_ERASER:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("LMB pressed! Erasing...")
                LMBpressed = True
                currX = event.pos[0]
                currY = event.pos[1]
                prevX = event.pos[0]
                prevY = event.pos[1]

            if event.type == pygame.MOUSEMOTION:
                print("Position of the mouse:", event.pos)
                if LMBpressed:
                    currX = event.pos[0]
                    currY = event.pos[1]
                    draw_eraser(currX, currY, THICKNESS)
                    prevX = currX
                    prevY = currY

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                print("LMB released!")
                LMBpressed = False
                clear_eraser_layer()
            
    screen.fill(colorWHITE)
    screen.blit(line_layer, (0, 0))
    screen.blit(rectangle_layer, (0, 0))
    screen.blit(circle_layer, (0, 0))
    screen.blit(eraser_layer, (0, 0))
    pygame.display.flip()

pygame.quit()
