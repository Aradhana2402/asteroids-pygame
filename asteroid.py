import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (radius, radius), radius, 2)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    def split(self):
        # Always destroy this asteroid
        self.kill()

        # If already too small, stop
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Pick random angle for splitting
        angle = random.uniform(20, 50)

        # Two new velocity vectors rotated from current velocity
        vel1 = self.velocity.rotate(angle) * 1.2
        vel2 = self.velocity.rotate(-angle) * 1.2

        # New radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Spawn two smaller asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = vel1
        asteroid1.add(*self.containers)

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = vel2
        asteroid2.add(*self.containers)
