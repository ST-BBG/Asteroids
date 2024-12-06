import pygame
pygame.init()
from constants import *
from player import Player

fps = pygame.time.Clock()
dt = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

updatable.add(player)
drawable.add(player)

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0, 0, 0))
        for drawy in drawable:
            drawy.draw(screen)
        pygame.display.flip()
        dt = fps.tick(60) / 1000
        for updaty in updatable:
            updaty.update(dt)

if __name__ == "__main__":
    main()
    game_loop()