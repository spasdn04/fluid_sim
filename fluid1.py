import numpy as np
import pygame as pg

pg.init()
WIDTH = 400
HEIGHT = 400
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('fluid simulator')
BLACK = (0, 0, 0)
RED = (255, 0, 0)
x, y = 200, 200
g = 9.81
velocity = 10
t = 0
run = True
while run:
    keys = pg.key.get_pressed()
    pg.time.delay(100)
    for event in pg.event.get():
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            run = False
    
    if y+g*t**2/2 < 380:
        t += 0.1
    else:
        t = 0
    
    print(t)
    if keys[pg.K_LEFT]:
        x -= velocity
    if keys[pg.K_RIGHT]:
        x += velocity
    if keys[pg.K_UP]:
        y -= velocity
    if keys[pg.K_DOWN]:
        y += velocity
    
    window.fill(BLACK)
    pg.draw.circle(window, RED, (x, y+g*t**2/2), 10, 2)
    pg.display.update()

pg.quit()