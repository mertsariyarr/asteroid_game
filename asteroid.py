import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            first_new_asteroid = self.velocity.rotate(random_angle)
            second_new_asteroid = self.velocity.rotate(-random_angle)
            first_new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            second_new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asto1 = Asteroid(self.position.x, self.position.y, first_new_asteroid_radius)
            asto2 = Asteroid(self.position.x, self.position.y, second_new_asteroid_radius)
            asto1.velocity += first_new_asteroid * 1.2
            asto2.velocity += second_new_asteroid * 1.2