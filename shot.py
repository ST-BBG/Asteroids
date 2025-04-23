import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(direction)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt * PLAYER_SHOOT_SPEED)