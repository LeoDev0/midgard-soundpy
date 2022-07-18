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

    # Get keystrokes event status (clicked or not)
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
            
            if event.key == pygame.K_F5:
                play_sound(pygame.K_F5, 'sounds/uepa.mp3')

            if event.key == pygame.K_F6:
                play_sound(pygame.K_F6, 'sounds/quem-disse-que-isso-e-problema-meu.mp3')

            if event.key == pygame.K_F7:
                play_sound(pygame.K_F7, 'sounds/coquinha-vai-tomar-no-cu.mp3')

            if event.key == pygame.K_F8:
                play_sound(pygame.K_F8, 'sounds/bolsonaro.mp3')

            if event.key == pygame.K_F9:
                play_sound(pygame.K_F9, 'sounds/ain-cigarrinho.mp3')

            if event.key == pygame.K_F10:
                play_sound(pygame.K_F10, 'sounds/ain-cafezinho.mp3')
    
    title_font = pygame.font.Font('freesansbold.ttf', 30)
    shortcuts_font = pygame.font.Font('freesansbold.ttf', 20)

    title_text = title_font.render('Shortcuts:', True, (255, 255, 255))

    screen.blit(title_text, (10, 10))
    screen.blit(shortcuts_font.render('[F1] - uuui', True, (255, 255, 255)), (50, 50))
    screen.blit(shortcuts_font.render('[F2] - cala-boca-puta', True, (255, 255, 255)), (50, 80))
    screen.blit(shortcuts_font.render('[F3] - me-apaixonei', True, (255, 255, 255)), (50, 110))
    screen.blit(shortcuts_font.render('[F4] - tome', True, (255, 255, 255)), (50, 140))
    screen.blit(shortcuts_font.render('[F5] - uepa', True, (255, 255, 255)), (50, 170))
    screen.blit(shortcuts_font.render('[F6] - quem-disse-que-isso-e-problema-meu', True, (255, 255, 255)), (50, 200))
    screen.blit(shortcuts_font.render('[F7] - coquinha-vai-tomar-no-cu', True, (255, 255, 255)), (50, 230))
    screen.blit(shortcuts_font.render('[F8] - bolsonaro', True, (255, 255, 255)), (50, 260))
    screen.blit(shortcuts_font.render('[F9] - ain-cigarrinho', True, (255, 255, 255)), (50, 290))
    screen.blit(shortcuts_font.render('[F10] - ain-cafezinho', True, (255, 255, 255)), (50, 320))

    pygame.display.update()


# Download audio (mp3) file from youtube videos
# https://www.y2meta.com/pt98

# Edit/Cut audios
# https://mp3cutterpro.com/en1