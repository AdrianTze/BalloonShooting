from random import random
from turtle import heading, width
import pygame


class Balloon(pygame.sprite.Sprite):

    def __init__(self, speed, x, y, constraint) -> None:
        super().__init__()
        self.image = pygame.image.load(
            'graphics/balloon2.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = speed  # declare the speed of the balloon
        self.constraint_y_max = constraint

        # to set the timer for changing movement
        self.change_cooldown = 2000  # milliseconds

    def update(self) -> None:
        self.rect.y += self.speed
        #current_time = pygame.time.get_ticks()
        # if current_time % self.change_cooldown == 0:
        #    print('changed')
        #    self.speed = -self.speed
        self.checkposition()

    def checkposition(self):
        if self.rect.y <= 0:
            self.speed = 1
        elif self.rect.y >= (self.constraint_y_max - self.rect.height):
            self.speed = -1
