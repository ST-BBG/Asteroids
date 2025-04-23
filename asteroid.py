import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position.x), int(self.position.y)), self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(50, 20)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid =  Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = pygame.Vector2(int(self.velocity.x) * 1.2, int(self.velocity.y) * 1.2).rotate(random_angle)
            asteroid =  Asteroid(self.position.x, self.position.y, new_radius)     
            asteroid.velocity = pygame.Vector2(int(self.velocity.x) * 1.2, int(self.velocity.y) * 1.2).rotate(-random_angle)

