import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # automatically add to containers if defined
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other_circle):
        """Return True if this circle collides with another CircleShape"""
        distance = self.position.distance_to(other_circle.position)
        return distance <= (self.radius + other_circle.radius)

