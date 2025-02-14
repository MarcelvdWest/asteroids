import pygame


# Base class for game object
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
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

    def split(self):
        self.kill()

    def collision_check(self, other_circle):
        distance_between = self.position.distance_to(other_circle.position)

        if self.radius + other_circle.radius > distance_between:
            return True
        return False
