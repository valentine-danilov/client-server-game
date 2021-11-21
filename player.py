import pygame
import uuid


class Player:
    def __init__(self, id, x, y, width, height, color):
        self.id = id
        self.x = x
        self.y = y
        self.width = width
        self.height = width
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 6

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def getId(self):
        return self.id

    def toString(self):
        return "Player {}.{} {}x{}".format(self.x, self.y, self.width, self.height)
