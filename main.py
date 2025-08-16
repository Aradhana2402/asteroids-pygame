import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)

    # Create game objects
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        dt = clock.tick(60) / 1000.0  # Convert ms → seconds

        # 2. Update
        for obj in updatable:
            obj.update(dt)

        # 3. Collision checks
        # Player vs Asteroid
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game Over!")
                pygame.quit()
                sys.exit()

        # Shot vs Asteroid
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()   # <-- splitting logic
                    shot.kill()

        # 4. Draw
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
