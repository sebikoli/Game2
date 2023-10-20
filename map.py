import pygame as py
import settings as set


class Map:
    def __init__(self) -> None:
        self.file = open("Map.csv", "r")
        self.file_csv_list = []
        self.get_csv()
        self.mapparts = py.image.load("mappart1.png")
        self.picture_list = []
        self.picture_getter()
        self.tile_list = []
        self.tile_creator()

    def get_csv(self):
        lines = self.file.readlines()
        for a in lines:
            splitted_lines = a.split(",")
            self.file_csv_list.append(splitted_lines)

    def picture_getter(self):
        x = 0
        y = -set.ORIGINALXTILE
        for a in range(1, 9):
            x = 0
            y += set.ORIGINALXTILE
            for b in range(1, 18):
                self.picture_list.append(py.transform.scale(self.mapparts.subsurface(x, y, set.ORIGINALXTILE, set.ORIGINALXTILE), [set.NEWXTILE, set.NEWXTILE]))
                x += set.ORIGINALXTILE

    def tile_creator(self):
        y = -set.NEWXTILE
        x = -set.NEWXTILE
        for a in range(len(self.file_csv_list)):
            line = self.file_csv_list[a]
            x = -set.NEWXTILE
            y += set.NEWXTILE
            for b in line:
                running_picture = self.picture_list[int(b)]
                x += set.NEWXTILE
                tile = Tile(running_picture, x, y)
                self.tile_list.append(tile)

    def paint(self, display):
        for a in self.tile_list:
            a.paint(display)


class Tile:
    def __init__(self, picture, coordinate1, coordinate2) -> None:
        self.picture = picture
        self.rect = py.Rect(coordinate1, coordinate2, set.NEWXTILE, set.NEWXTILE)

    def paint(self, display):
        display.blit(self.picture, self.rect)
