import pygame as pg
import random as rd

pg.init()
WIDTH = 400
HEIGHT = 400
window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('fluid simulator')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
#Aquí se mete el código estático / definir variables
velocity = [3,3]
aceleration = [0.1,0.2]
gravity = 9.81
mass = 1
radius = 10
density = 3
time = 1

class BoxSimulation():
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
    
    def box(self):
        pg.draw.rect(window, self.color, pg.Rect(0,0,self.width,self.height), 2)

class Particle():
    def __init__(self, position, velocity, aceleration, density, color, radius, time):
        self.position = position
        self.velocity = velocity
        self.aceleration = aceleration
        self.density = density
        self.color = color
        self.radius = radius
        self.time = time

    def circle(self):
        for i in range(self.density):
            pg.draw.circle(window, self.color, (self.position[0]+i*2*self.radius, self.position[1]), self.radius)
    
    def collision(self):
        positionx = self.position[0] + self.radius
        positiony = self.position[1] + self.radius
        
        if positionx <= 20:
            self.velocity[0] *= -1
        
        if positionx >= 390:
            self.velocity[0] *= -1
            
        if positiony >= 390:
            self.velocity[1] *= -1
            
        if positiony <= 20:
            self.velocity[1] *= -1

    def movement(self):
        new_position = []
        for i in range(len(self.position)):
            new_position.append(self.position[i] + self.velocity[i] * self.time + (self.aceleration[i] * self.time**2) / 2)
        self.position = tuple(new_position)
    

box = BoxSimulation(400, 400, RED)
particle = Particle([rd.randint(0, 400), rd.randint(0, 200)], [0,0], [0, gravity], 1, BLACK, 10, 1)


run = True
while run:
    time +=1
    
    keys = pg.key.get_pressed()
    pg.time.delay(100)
    for event in pg.event.get():
        if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
            run = False
    window.fill(WHITE)
    
    # Aquí se mete código dinámico
    box.box()
    
    particle.circle()
    particle.movement()
    particle.collision()
    print(particle.position)
    
    pg.display.flip()
pg.quit()