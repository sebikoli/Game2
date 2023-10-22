import menu
import pygame

SIZEX = 1500
SIZEY = 700
ORIGINALXTILE = 16
NEWXTILE = int(menu.event_part_2["size"])
ORIGINALPLAYER = 32
NEWPLAYER = int(menu.event_part_2["playersize"])
CONTROLS = menu.event_part_2["wasd"]
if CONTROLS is True:
    up = pygame.K_w
    down = pygame.K_s
    right = pygame.K_d
    left = pygame.K_a
else:
    up = pygame.K_UP
    down = pygame.K_DOWN
    right = pygame.K_RIGHT
    left = pygame.K_LEFT
