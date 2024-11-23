import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)

        one = self.velocity.rotate(random_angle)
        two = self.velocity.rotate(-random_angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_rad)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_rad)

        new_asteroid1.velocity += one * 1.2
        new_asteroid2.velocity += two

    def update(self, dt):
        self.position += self.velocity * dt
