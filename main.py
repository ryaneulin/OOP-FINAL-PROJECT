import pygame
import sys
from menu import show_menu
from dialogue import run_dialogue
from game_world import run_game_world

def main():
    pygame.init()

    w_width, w_height = 800, 600
    screen = pygame.display.set_mode((w_width, w_height))
    pygame.display.set_caption("OOP Final Project")

    current_state = "menu"
    running = True

    while running:
        if current_state == "menu":
            result = show_menu(screen)
            if result == "quit":
                running = False
            else:
                current_state = result

        elif current_state == "dialogue":
            result = run_dialogue(screen)
            if result == "quit":
                running = False
            else:
                current_state = result

        elif current_state == "game_world":
            result = run_game_world(screen)
            if result == "quit":
                running = False
            else:
                current_state = result

        else:
            print(f"Unknown state: {current_state}")
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
