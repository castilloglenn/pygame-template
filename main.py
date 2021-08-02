import pygame as game
import xml.etree.ElementTree as xml
import os, sys


def clearResourcesAndQuit():
    game.display.quit()
    game.quit()
    sys.quit()


# Global default variables
strings = {}


if __name__ == '__main__':
    # Centering the game window on the screen
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    # Accessing XML data and saving to a dictionary for later use
    tree = xml.parse('strings.xml')
    root = tree.getroot()
    for element in root: strings[element.tag] = element.text

    # Pygame initialization process
    game.init()
    game.display.set_caption(strings['gameTitle'])
    game.display.set_mode((640, 480))

    # Game loop
    while True:
        for event in game.event.get():
            if event.type == game.QUIT: clearResourcesAndQuit()
