import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.reload_timer = 0   

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * (dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.reload_timer > 0:
            self.reload_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt * (-1))
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt * (-1))
        if keys[pygame.K_SPACE]:
            if self.reload_timer <= 0:
                self.shoot(self.position.x, self.position.y, self.rotation)
                self.reload_timer += PLAYER_SHOT_COOLDOWN
            print(self.reload_timer)

    def shoot(self, launch_x, launch_y, direction):
        from shot import Shot
        shot = Shot(launch_x, launch_y, direction)
