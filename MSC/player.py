import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, right_images, left_images, down_images, up_images):
        super().__init__()

        self.image = pygame.image.load(right_images[0])  # Default facing right
        self.rect = self.image.get_rect(topleft=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5

        # Set up animation images for all directions
        self.right_images = [pygame.image.load(img) for img in right_images]
        self.left_images = [pygame.image.load(img) for img in left_images]
        self.down_images = [pygame.image.load(img) for img in down_images]
        self.up_images = [pygame.image.load(img) for img in up_images]
        
        self.direction = "right"  # Initial direction
        self.animation_frame = 0

    def update(self):
        """Update the player animation and position"""
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

        # Switch animation based on movement direction
        if self.velocity.x > 0:
            self.direction = "right"
        elif self.velocity.x < 0:
            self.direction = "left"
        elif self.velocity.y > 0:
            self.direction = "down"
        elif self.velocity.y < 0:
            self.direction = "up"

        # Animation handling
        if self.direction == "right":
            self.animate(self.right_images)
        elif self.direction == "left":
            self.animate(self.left_images)
        elif self.direction == "down":
            self.animate(self.down_images)
        elif self.direction == "up":
            self.animate(self.up_images)

    def animate(self, images):
        """Handle animation by cycling through the images"""
        self.animation_frame += 1
        if self.animation_frame >= len(images):
            self.animation_frame = 0
        self.image = images[self.animation_frame]
