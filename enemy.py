import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, images):
        super().__init__()
        self.image = pygame.image.load(images[0])  # Default enemy image
        self.rect = self.image.get_rect(topleft=(x, y))

        self.images = [pygame.image.load(img) for img in images]
        self.animation_frame = 0

    def update(self):
        """Update the enemy animation"""
        self.animate(self.images)

    def animate(self, images):
        """Handle animation by cycling through the images"""
        self.animation_frame += 1
        if self.animation_frame >= len(images):
            self.animation_frame = 0
        self.image = images[self.animation_frame]
