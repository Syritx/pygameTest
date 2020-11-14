import pygame as pyg
import coordinate as coord

class user:

    sprite = pyg.image.load('t.png')
    position = coord.position(0,0)

    def __init__(self, position):
        global sprite

        self.sprite = pyg.transform.scale(self.sprite, (100,100))
        self.position = position