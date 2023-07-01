import random
import pygame

class Food:
    def __init__(self):
        self.x = random.randint(0, 79) * 10
        self.y = random.randint(0, 59) * 10

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 10, 10))
