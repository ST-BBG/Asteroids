import pygame
pygame.init()
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

fps = pygame.time.Clock()
dt = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
   
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable,)
Shot.containers = (shots, updatable, drawable)

player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
theasteroidfield = AsteroidField()

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0, 0, 0))
        dt = fps.tick(60) / 1000
        updatable.update(dt)
        for drawables in drawable:
            drawables.draw(screen)
        pygame.display.flip()
        for Asteroid in asteroids:
            if Asteroid.collision(player):
                print("Game over!")
                import sys
                raise sys.exit([0])
        for Shot in shots:
            for Asteroid in asteroids:
                if Shot.collision(Asteroid):
                    Asteroid.kill()
                    Shot.kill()
        
        

if __name__ == "__main__":
    main()
    game_loop()