import pygame
import pygame_gui
from pygame import mixer
import os, random
from pathlib import Path

pygame.init()
pygame.mixer.init()

pygame.display.set_caption('Radio Test')
window_surface = pygame.display.set_mode((480, 320))

background = pygame.Surface((480, 320))
background.fill(pygame.Color('#000000'))
manager = pygame_gui.UIManager((480, 320))


def exit_radio():
    mixer.music.stop()
    mixer.music.unload()


def main():
    fnv_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (160, 50)), text='FNV OST',
                                              manager=manager)
    inv_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 60), (160, 50)), text='Radio',
                                              manager=manager)

    clock = pygame.time.Clock()
    is_running = True

    while is_running:
        time_delta = clock.tick(60) / 1000.0
        thing = Path('radio_FNV')
        songs_ = []
        with os.scandir('radio_FNV/') as entries:
            for entry in entries:
                pygame.mixer.music.load(entry)
                pygame.mixer.music.play()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == fnv_button:
                    play_music(load_music("radio_FNV"))

                if event.ui_element == inv_button:
                    exit_radio()

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()


# Loads all files for that specific station in random order before playing
def load_music(station):
    songs = []

    dir = Path('radio_FNV')

    for song in os.scandir(dir):
        songs.append(os.path.basename(song))

    random.shuffle(songs)
    print(songs)
    os.chdir(dir)
    return songs


def play_music(songs):
    for song in songs:
        print(song)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

    play_music(songs)


if __name__ == "__main__":
    main()
