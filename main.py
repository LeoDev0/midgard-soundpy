import time
import pygame
from pygame import mixer

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((600, 400))

# Set background image
background = pygame.image.load('images/background.jpg')
background = pygame.transform.scale(background, (600, 400))

# Caption and Icon
pygame.display.set_caption('Midgard SoundPy')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

def play_sound(KEY: int, sound_path: str) -> None:
    print(KEY)
    pygame.mixer.music.stop()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    # while pygame.mixer.music.get_busy():  # wait for music to finish playing
    #     time.sleep(1)

# Pause/Unpause playing audio  
def pause() -> None:
   pygame.mixer.music.pause() if pygame.mixer.music.get_busy() else pygame.mixer.music.unpause()
    

# Application loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))

    # Get keystokes event status (clicked or not)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause()

            if event.key == pygame.K_F1:
                play_sound(pygame.K_F1, 'sounds/uuui.mp3')

            if event.key == pygame.K_F2:
                play_sound(pygame.K_F2, 'sounds/cala-boca-puta.mp3')
            
            if event.key == pygame.K_F3:
                play_sound(pygame.K_F3, 'sounds/me-apaixonei.mp3')

            if event.key == pygame.K_F4:
                play_sound(pygame.K_F4, 'sounds/tome.mp3')
    
    # show_shorcut_to_audios()
    title_font = pygame.font.Font('freesansbold.ttf', 30)
    shortcuts_font = pygame.font.Font('freesansbold.ttf', 20)

    title_text = title_font.render('Shortcuts:', True, (255, 255, 255))

    screen.blit(title_text, (10, 10))
    screen.blit(shortcuts_font.render('[F1] - uuui', True, (255, 255, 255)), (50, 50))
    screen.blit(shortcuts_font.render('[F2] - cala-boca-puta', True, (255, 255, 255)), (50, 80))
    screen.blit(shortcuts_font.render('[F3] - me-apaixonei', True, (255, 255, 255)), (50, 110))
    screen.blit(shortcuts_font.render('[F4] - tome', True, (255, 255, 255)), (50, 140))

    pygame.display.update()


# Download audio (mp3) file from youtube videos
# https://www.y2meta.com/pt98

# Edit/Cut audios
# https://mp3cutterpro.com/en1