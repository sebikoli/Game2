import pygame
import settings as set
import sprites as spr
import map
import camera as cam
pygame.init()

close = 1
personal_event = pygame.USEREVENT
close = 0
display = pygame.display.set_mode([set.SIZEX, set.SIZEY])
clock = pygame.time.Clock()
player = spr.Player()
karte = map.Map()
camera = cam.Camera(player)

while close == 0:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            close = 1
    display.fill([119, 16, 72])
    karte.paint(display, camera)
    player.paint(display)
    player.move()
    camera.player_watcher()
    pygame.display.update()
    clock.tick(60)
