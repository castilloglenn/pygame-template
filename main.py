import pygame
from object import Object
import xml.etree.ElementTree as xml
import os, sys


class Game:
    def __init__(self):
        # Storing default values stored from the config folder
        self.strings = {}
        self.values = {}

        # Centering the game window on the screen
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        
        # Accessing XML data and saving to a dictionary for later use
        stringsTree = xml.parse('config/strings.xml')
        stringsRoot = stringsTree.getroot()
        for stringsElement in stringsRoot: self.strings[stringsElement.tag] = stringsElement.text

        valuesTree = xml.parse('config/values.xml')
        valuesRoot = valuesTree.getroot()
        for valuesElement in valuesRoot:
            if valuesElement.tag[0:3] == 'int':
                self.values[valuesElement.tag] = int(valuesElement.text)
            elif valuesElement.tag[0:5] == 'float':
                self.values[valuesElement.tag] = float(valuesElement.text)
        
        # Pygame initialization process
        pygame.init()
        pygame.display.set_caption(f"{self.strings['gameTitle']} {self.strings['gameVersion']}")
        pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()

        # Storing values that is needed for the game
        self.last_mouse_pos = None
        self.pause_timeout = 0
        
        # Storing all the spritesheets of entities
        self.ship = Object('Ship')


    def run_main(self):
        # Game loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.clear_resources()
                if event.type == pygame.MOUSEBUTTONDOWN: self.mouse_click_events(event)
                if event.type == pygame.MOUSEMOTION: self.mouse_drag_events(event)
            
            # Key pressing events (holding keys applicable)
            keys = pygame.key.get_pressed()

            # Avoiding instant unpause by setting an initial timeout of X second to pause the game
            self.pause_timeout += 1

            # the hotkey here must be the button to pause the game, space is just placeholder
            if keys[pygame.K_SPACE] and self.pause_timeout >= (self.values['intFrameRate']): 
                # This shall pause the game
                self.pause_timeout = 0
                pass
            else: self.key_events(keys)


    def mouse_click_events(self, event):
        # If the user clicked on left mouse button
        if event.button == 1: pass

        # If the user clicked on the right mouse button
        if event.button == 3: pass

        # If the user scrolls the mouse wheel upward
        if event.button == 4:  pass

        # If the user scrolls the mouse wheel downward
        if event.button == 5:  pass


    def mouse_drag_events(self, event):
        # This variable always saves the last mouse location to be used by the
        #   gameKeyEvents() function, because we can't always get the location
        #   of the mouse if the only event is key press
        self.last_mouse_pos = event.pos

        # Making sure the user only holds one button at a time
        if event.buttons[0] + event.buttons[1] + event.buttons[2] == 1:
            # relativeLocation = getRelativeLocation(event.pos)

            # If the user is dragging the mouse with left mouse button
            if event.buttons[0] == 1: pass

            # If the user is dragging the mouse with the right mouse button
            if event.buttons[2] == 1: pass


    def key_events(self, keys):
        # If the user pressed the "del" key, (enter explanation here)
        if keys[pygame.K_DELETE]: pass

        # If the user pressed the "a" key, (enter explanation here)
        if keys[pygame.K_a]: pass

        # If the user pressed the "d" key, (enter explanation here)
        if keys[pygame.K_d]: pass


    def refresh_display(self):
        pygame.display.update()
        self.clock.tick(self.values['intFrameRate'])

    
    def clear_resources(self):
        pygame.display.quit()
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run_main()
