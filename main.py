import pygame
pygame.init()
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)
Shot.containers = (shots, updatable, drawable)

def main():
    game_clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    a = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for gobject in updatable:
            gobject.update(dt)
        for gobject in drawable:
            gobject.draw(screen)
        for gobject in asteroids:
            p.collide(gobject)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()
        pygame.display.flip()

        dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()
