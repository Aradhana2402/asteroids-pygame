import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(x, y, radius, self.containers)
        else:
            super().__init__(x, y, radius)
        self.rotation = 0
        self.shot_timer = 0  # 🚀 cooldown timer

    def draw(self, screen):
        # ship is a triangle
        points = []
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = forward.rotate(120)
        left = forward.rotate(-120)
        points.append(self.position + forward * self.radius)
        points.append(self.position + right * self.radius * 0.6)
        points.append(self.position + left * self.radius * 0.6)
        pygame.draw.polygon(screen, "white", points, 1)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rotation -= 180 * dt
        if keys[pygame.K_RIGHT]:
            self.rotation += 180 * dt
        if keys[pygame.K_UP]:
            forward = pygame.Vector2(0, -1).rotate(self.rotation)
            self.velocity += forward * 200 * dt
        if keys[pygame.K_SPACE]:  
            self.shoot()

        # 🚀 Cooldown countdown
        if self.shot_timer > 0:
            self.shot_timer -= dt

        self.position += self.velocity * dt

    def shoot(self):
        if self.shot_timer > 0:  # 🚫 still cooling down
            return  

        # Create new bullet
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED

        # Reset cooldown
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

