import pygame
from pygame.locals import *
import math

class Car:
    def __init__(self, x, y, speed, screen):
        self.x = x
        self.y = y
        self.speed = speed / 200
        self.screen = screen
        self.width = 50
        self.height = 24.5
        self.angle = 0
        self.image = pygame.image.load('Assets\simple-travel-car-top_view.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.imageTransform = self.image

    def draw(self):
        self.rect = self.imageTransform.get_rect(center=self.image.get_rect(center=(self.x, self.y)).center)
        self.car = self.screen.blit(self.imageTransform, self.rect)
        # self.rect = pygame.draw.rect(self.screen, "red", pygame.Rect(self.x, self.y, self.width, self.height))
    
    def move(self, dt):
        self.x += self.speed * math.cos(self.angle) * dt
        self.y += self.speed * math.sin(self.angle) * dt

    def rotate(self, angle):
        self.angle += angle
        self.imageTransform = pygame.transform.rotate(self.image, -(self.angle) * 180 / math.pi)