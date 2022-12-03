import time

import pygame
from pygame import mixer
import os, random
from pathlib import Path
import button
import math
import random

# draw rect but with transparency
def draw_rect_alpha(surf, color, rect):
    shape = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
    pygame.draw.rect(shape, color, shape.get_rect())
    surf.blit(shape, rect)


def display_text(surf, x_coord, y_coord, color, text=''):
    """
    :param color: tuple
    :type x_coord: int
    :type y_coord: int
    :type text: String
    :type surf: Surface
    """
    TEXT_COL = color

    font = pygame.font.SysFont('arial', 20)
    text = font.render(text, False, TEXT_COL)
    surf.blit(text, (x_coord, y_coord))

def display_text_small(surf, x_coord, y_coord, color, text=''):
    """
    :param color: tuple
    :type x_coord: int
    :type y_coord: int
    :type text: String
    :type surf: Surface
    """
    TEXT_COL = color

    font = pygame.font.SysFont('arial', 15)
    text = font.render(text, False, TEXT_COL)
    surf.blit(text, (x_coord, y_coord))

def load_music(station):
    songs = []

    dir = Path(station)

    for song in os.scandir(dir):
        songs.append(os.path.basename(song))

    random.shuffle(songs)
    return songs


def play_music(songs, flag, i, folder_name):
    count = i
    if not flag:
        mixer.music.stop()
        mixer.music.unload()
        file = "../raspip-boy/" + folder_name + "/" + songs[count]
        mixer.music.load(file)
        for i in range(len(songs)):
            mixer.music.queue("../raspip-boy/" + folder_name + "/" + songs[i])
        mixer.music.play()

def exit_radio():
    mixer.music.stop()
    mixer.music.unload()


'''
The Radio Class for the PipBoy
    This will be where the radio goes, it should display the radio as well as a little visual thing on the side
    but that's for later
    Notes:
    Fix Radio buttons
    Theory- when set to false, what happens is the function is called and it get uncalled, unlinke when we
    use TRUE or something along those lines. Further testing may be need, but perhaps changing how the play music 
    function works could help??
'''


class Radio:

    def __init__(self):
        self.color = (51, 140, 48)
        self.main_color = (88, 243, 100, 180)
        self.x_r = 10
        self.y = 55
        self.x_l = 230
        self.menu_width = 200
        self.height = 45
        self.fnv_button = button.Button((0, 0, 0, 0), self.x_r, self.y, self.menu_width, 30, "")
        self.backup_button = button.Button((0, 0, 0, 0), self.x_r, self.y + 30, self.menu_width, 30, "")
        self.meme_button = button.Button((0, 0, 0, 0), self.x_r, self.y + 60, self.menu_width, 30, "")
        self.nightcore_button = button.Button((0, 0, 0, 0), self.x_r, self.y + 90, self.menu_width, 30, "")
        self.off_button = button.Button((0,0,0,0), self.x_r, self.y + 150, self.menu_width, 30, "")

        self.frequency = 35
        self.amplitude = 30
        self.overallY = 300

        self.counter = 0
        self.num = 0

    def draw(self, surf):
        rect = (self.x_r, self.y), (200, 235)
        draw_rect_alpha(surf, self.color, rect)

        rect = (self.x_l, self.y), (235, 235)
        draw_rect_alpha(surf, self.color, rect)

    def squiggle(self, surf, num):
        no_pts = surf.get_width()
        for i in range(no_pts):
            i += 235
            x = (i / no_pts * 2 * math.pi) + num
            y = (self.amplitude * math.cos(x * self.frequency)) + self.overallY - 210
            if i > 235:
                pygame.draw.aaline(surf, (100, 252, 127), prev_pt, (i, y))
            prev_pt = (i, y)

    def final_dance_ultra(self, surf, tick):
        clock = pygame.time.Clock()
        if self.counter == 1:
            self.squiggle(surf, 0)
            clock.tick(tick)
        elif self.counter == 2:
            self.squiggle(surf, 90)
            clock.tick(tick)
        elif self.counter == 3:
            self.squiggle(surf, 180)
            clock.tick(tick)
        elif self.counter == 4:
            self.squiggle(surf, 270)
            clock.tick(tick)
        elif self.counter == 5:
            self.squiggle(surf, 360)
            clock.tick(tick)
        elif self.counter == 6:
            self.squiggle(surf, 450)
            clock.tick(tick)
        elif self.counter == 7:
            self.squiggle(surf, 540)
            clock.tick(tick)
        else:
            self.squiggle(surf, 630)
            clock.tick(tick)
            self.counter = 0

    def read_file(self, surf, filename=''):
        f = open(filename, "r")

        x = 235
        y = 135
        for line in f:
            rect = (self.x_l, y), (x, 30)
            draw_rect_alpha(surf, (51, 140, 48, 100), rect)
            #=text = line
            display_text_small(surf, self.x_l + 5, y, (100, 252, 127), line.strip('\n'))
            y += 30
        f.close()

    def tab(self, surf, y_increase, in_button, frequency, folder_name='', filename='', text=''):

        if in_button.is_pressed(surf):
            rect = (self.x_r, self.y + y_increase), (200, 30)
            draw_rect_alpha(surf, self.main_color, rect)

            display_text(surf, self.x_r + 5, self.y + (y_increase + 3), (52, 68, 52), text)
            self.frequency = frequency
            self.counter += 1
            self.final_dance_ultra(surf, 5)
            self.read_file(surf, filename)
            if in_button.is_pressed_promise(surf):
                play_music(load_music(folder_name), False, 0, folder_name)
        else:
            display_text(surf, self.x_r + 5, self.y + (y_increase + 3), (100, 252, 127), text)
            play_music(load_music(folder_name),  True, 0, folder_name)

    def off(self, surf, y_increase, in_button, text=''):

        if in_button.is_pressed(surf):
            rect = (self.x_r, self.y + y_increase), (200, 30)
            draw_rect_alpha(surf, self.main_color, rect)

            display_text(surf, self.x_r + 5, self.y + (y_increase + 3), (52, 68, 52), text)
            exit_radio()

        else:
            display_text(surf, self.x_r + 5, self.y + (y_increase + 3), (100, 252, 127), text)

    def menu(self, surf):
        self.tab(surf, 0, self.fnv_button, 30, "radio_FNV", "radio_FNV.txt", "Fallout New Vegas")
        self.tab(surf, 30, self.backup_button, 0, "radio_TEST", "radio_FNV.txt", "Fallout Old Vegas") # edit
        self.tab(surf, 60, self.backup_button, 30, "radio_FUN", "radio_FUN.txt", "Kamila Radio")
        self.tab(surf, 90, self.backup_button, 0, "radio_NIGHTCORE", "radio_NIGHTCORE.txt", "Nightcore")
        self.off(surf, 150, self.off_button, "Turn Off Radio")