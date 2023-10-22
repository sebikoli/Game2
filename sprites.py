import pygame as py
import settings as set


class Player:
    def __init__(self) -> None:
        self.picture = py.image.load("Ugly_player.png")
        self.pictures_left = []
        self.pictures_right = []
        self.pictures_up = []
        self.pictures_down = []
        self.picture_getter()
        self.rect = py.Rect(100, 100, set.NEWPLAYER, set.NEWPLAYER)
        self.speedx = 0
        self.speedy = 0
        self.running_picture = self.pictures_down[0]
        self.speed = 2
        self.number = 0

    def picture_getter(self):
        x = 0
        for a in range(1, 5):
            self.pictures_down.append(py.transform.scale(self.picture.subsurface(x, 0, 32, 32), [set.NEWPLAYER, set.NEWPLAYER]))
            self.pictures_left.append(py.transform.scale(self.picture.subsurface(x, 32, 32, 32), [set.NEWPLAYER, set.NEWPLAYER]))
            self.pictures_right.append(py.transform.scale(self.picture.subsurface(x, 64, 32, 32), [set.NEWPLAYER, set.NEWPLAYER]))
            self.pictures_up.append(py.transform.scale(self.picture.subsurface(x, 96, 32, 32), [set.NEWPLAYER, set.NEWPLAYER]))
            x += 32

    def paint(self, display):
        display.blit(self.running_picture, self.rect)

    def move(self):
        all_keys = py.key.get_pressed()
        if all_keys[set.up] is True:
            self.rect.y = self.rect.y-self.speed
            self.running_picture = self.pictures_up[int(self.number)]
        if all_keys[set.down] is True:
            self.rect.y = self.rect.y+self.speed
            self.running_picture = self.pictures_down[int(self.number)]
        if all_keys[set.left] is True:
            self.rect.x = self.rect.x-self.speed
            self.running_picture = self.pictures_left[int(self.number)]
        if all_keys[set.right] is True:
            self.rect.x = self.rect.x+self.speed
            self.running_picture = self.pictures_right[int(self.number)]
        self.number += 0.2
        if self.number >= 4:
            self.number = 0
