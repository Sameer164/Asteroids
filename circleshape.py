import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Say we want to inherit a class from CircleShape, and if that class contains containers as a class variable or instance variable
        # we want to initialize the super super class appropriately
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
    
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
    
    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    def has_collided(self, other_shape):
        dist = pygame.math.Vector2.distance_to(self.position, other_shape.position)
        return dist <= self.radius + other_shape.radius
