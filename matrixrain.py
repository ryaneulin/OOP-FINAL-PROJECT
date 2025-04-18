import pygame
import random

class MatrixRainEffect:
    def __init__(self, screen, font_size=20, rain_speed=9):
        self.screen = screen
        self.font_size = font_size
        self.font = pygame.font.SysFont("consolas", font_size, bold=True)
        self.rain_speed = rain_speed

        self.width, self.height = screen.get_size()
        self.columns = self.width // font_size
        self.chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*"
        self.drops = [random.uniform(0, self.height // font_size) for _ in range(self.columns)]
        self.last_rows = [-1] * self.columns

        self.fade_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

    def update_and_draw(self, dt):
        fade_strength = int(self.rain_speed * 1.5)
        fade_strength = max(9, min(40, fade_strength))  # Clamp fade
        self.fade_surface.fill((0, 0, 0, fade_strength))
        self.screen.blit(self.fade_surface, (0, 0))

        for i in range(self.columns):
            current_row = int(self.drops[i])

            if current_row != self.last_rows[i]:
                x = i * self.font_size
                y = current_row * self.font_size

                if y < self.height:
                    char = random.choice(self.chars)
                    surface = self.font.render(char, True, (0, 255, 0))
                    self.screen.blit(surface, (x, y))
                    self.last_rows[i] = current_row

            self.drops[i] += self.rain_speed * (1 / 60)

            if self.drops[i] * self.font_size > self.height and random.random() > 0.975:
                self.drops[i] = 0
                self.last_rows[i] = -1
