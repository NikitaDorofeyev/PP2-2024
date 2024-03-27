import pygame
import os

pygame.init()

screen = pygame.display.set_mode((500, 250))
screen_center = (250, 125)
current_directory = os.path.dirname(__file__)

# Import images
parent_directory = os.path.dirname(current_directory) 

def load_image(image_name, size):
    image_path = os.path.join(images_directory, image_name)
    return pygame.transform.scale(pygame.image.load(image_path), size)

# Load images from the images directory
images_directory = os.path.join(parent_directory, 'Music Player', 'images')
play_b = load_image('play-button.png', (75, 75))
pause_b = load_image('pause.png', (75, 75))
next_b = load_image('next.png', (75,75))
back_b = load_image('back.png', (75, 75))

# Import songs
songs_directory = os.path.join(parent_directory, 'Music Player', 'songs')

def load_song(song_name):
    return pygame.mixer.Sound(os.path.join(songs_directory, song_name))

# Load songs
songs = [
    load_song('song1.mp3'),
    load_song('song2.mp3'),
    load_song('song3.mp3'),
    load_song('song4.mp3'),
    load_song('song5.mp3'),
    load_song('song6.mp3')
]

pause = True
current_song = 0

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not pause:
                    pygame.mixer.pause()
                    pause = True
                else:
                    if current_song == 0:
                        songs[0].play()
                    pygame.mixer.unpause()
                    pause = False
                    
            elif event.key == pygame.K_RIGHT:
                pause = False
                pygame.mixer.stop()
                current_song = (current_song + 1) % len(songs)
                songs[current_song].play()
            elif event.key == pygame.K_LEFT:
                pause = False
                pygame.mixer.stop()
                current_song = (current_song - 1) % len(songs)
                songs[current_song].play()
    
    screen.fill((255, 255, 255))


    # Buttons positions
    pause_pos = pause_b.get_rect(center=screen_center)
    play_pos = play_b.get_rect(center=screen_center)
    back_pos = back_b.get_rect(center=(screen_center[0] - 125, screen_center[1]))
    next_pos = next_b.get_rect(center=(screen_center[0] + 125, screen_center[1]))

    # Pause and Play
    if pause:
        screen.blit(play_b, play_pos)
        
    else:
        screen.blit(pause_b, pause_pos)
    

    screen.blit(next_b, next_pos)
    screen.blit(back_b, back_pos)

    pygame.display.flip()

pygame.quit()