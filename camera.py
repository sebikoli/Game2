import pygame as py
import settings as set


class Camera:
    def __init__(self, player):
        self.player = player
        self.movex = 0
        self.movey = 0

    def player_watcher(self):
        self.movex = -self.player.rect.x
        self.movey = -self.player.rect.y

    def rect_changer(self, rect):
        cam_rect = py.Rect(rect.x + self.movex, rect.y + self.movey, rect.w, rect.h)
        return cam_rect
