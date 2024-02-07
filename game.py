import sys
import math
import random
import pygame
from pygame.locals import *

from Car import Car

width = 1000
height = 600

pygame.init()

screen = pygame.display.set_mode((width, height))
x = width / 2
y = height / 2
speed = 200

Car.__init__(Car, x, y, speed, screen)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('gray')

    Car.draw(Car)

    key = pygame.key.get_pressed()
    if key[K_w]:    
        Car.move(Car, 1)
    if key[K_s]:
        Car.move(Car, -0.5)
    if key[K_a]:
        Car.rotate(Car, -0.005)
    if key[K_d]:
        Car.rotate(Car, 0.005)


    pygame.display.flip()