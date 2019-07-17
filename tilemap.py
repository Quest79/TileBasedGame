import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
#from main import *


class Maps:
    def __init__(self, filename):
        self.data = []
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'map')
        fulldir = path.join(map_folder, filename)
        with open(fulldir, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(WIDTH / 2)
        y = -target.rect.y + int(HEIGHT / 2)

        # Lets limit scolling to map size, so we dont see empty space outside of walls
        x = min(0, x)
        y = min(0, y)
        x = max(x, -self.width+WIDTH)
        y = max(y, -self.height+HEIGHT)
        # y = max(-self.height, y)
        self.camera = pg.Rect(x, y, self.width, self.height)
