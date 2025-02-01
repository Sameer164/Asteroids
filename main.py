import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = [updatable, drawable]
    Asteroid.containers = [asteroids, updatable, drawable]
    AsteroidField.containers = [updatable]
    Shot.containers = [shots_group, updatable, drawable]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    astrofield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2)
    clock = pygame.time.Clock()
    pause = 60 # how much to pause
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.has_collided(player):
                print("Game Over")
                sys.exit(0)
        
        for asteroid in asteroids:
            for bullet in shots_group:
                if asteroid.has_collided(bullet):
                    bullet.kill()
                    asteroid.split()

        for objects in drawable:
            objects.draw(screen)

        pygame.display.flip()
        dt = clock.tick(pause) / 1000 # Pauses for 1/60th of a second and saves the time that has passed since being called last

if __name__ == "__main__":
    main()