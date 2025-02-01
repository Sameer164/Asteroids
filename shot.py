import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOT_SPEED, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, radius = SHOT_RADIUS):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt
