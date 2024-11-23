import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
            if self.radius <= ASTEROID_MIN_RADIUS:
                self.kill()
            else:
                split_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
                split_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
                split_asteroid1.velocity = self.velocity.rotate(random.uniform(-20, -50)) * 1.2
                split_asteroid2.velocity = self.velocity.rotate(random.uniform(20, 50)) * 1.2
                self.kill()
                return split_asteroid1, split_asteroid2

