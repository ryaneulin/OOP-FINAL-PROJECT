import pygame
import random
from matrixrain import MatrixRainEffect

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOX_COLOR = (50, 50, 50)
TEXT_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 600

# Dialogue lines
dialogue_lines = [
    "Welcome to the debug world!",
    "You're the only one who can fix the broken code.",
    "Complete the quests to restore order.",
    "Good luck, developer!"
]

def run_dialogue(screen):
    font = pygame.font.SysFont("arial", 28)
    clock = pygame.time.Clock()

    current_line = 0
    show_dialogue = True
    matrix = MatrixRainEffect(screen, font_size=20, rain_speed=9)

    while show_dialogue:
        screen.fill(BLACK)

        # Matrix Background Effect
        dt = clock.tick(60) / 1000
        matrix.update_and_draw(dt)

        # Draw dialogue box
        box_rect = pygame.Rect(50, HEIGHT - 150, WIDTH - 100, 100)
        pygame.draw.rect(screen, BOX_COLOR, box_rect)
        pygame.draw.rect(screen, WHITE, box_rect, 2)

        # Draw dialogue text
        text = font.render(dialogue_lines[current_line], True, TEXT_COLOR)
        screen.blit(text, (box_rect.x + 20, box_rect.y + 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_line += 1
                    if current_line >= len(dialogue_lines):
                        return "game_world"

        pygame.display.flip()
