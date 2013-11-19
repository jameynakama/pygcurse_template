#!/usr/bin/env python

import os
import sys

import pygame
from lib import pygcurse

from helpers.constants import Constants


# TODO:


class Game(object):
    def __init__(self):
        self.window = pygcurse.PygcurseWindow(Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT, "GAME NAME")
        pygame.mouse.set_visible(Constants.CONFIG.getboolean('game', 'mouse'))
        self.window.autoupdate = False
        # self.clock = pygame.time.Clock()

        font_name = Constants.CONFIG.get('game', 'font')
        font_size = Constants.CONFIG.getint('game', 'font_size')
        self.window.font = pygame.font.Font(os.path.join(Constants.RES_DIR, font_name), font_size)

        self.exit_game_loop = False

    def run(self):
        while 1:
            # self.clock.tick(Constants.FPS)

            self.window.setscreencolors(None, 'black', clear=True)
            self.window.fill(bgcolor=Constants.BG_COLOR, region=(1, 1, Constants.SCREEN_WIDTH - 2, Constants.SCREEN_HEIGHT - 2))

            # input
            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    sys.exit(0)

            # compute

            # draw
            self.render()

    def render(self):
        self.window.update()


def main():
    while 1:
        game = Game()
        game.run()


if __name__ == '__main__':
    main()
