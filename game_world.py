import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOX_COLOR = (50, 50, 50)
TEXT_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 600

# Player data
player = {"health": 100, "level": 1, "inventory": [], "experience": 0}

# Enemy data
enemies = [
    {"name": "Bug1", "health": 100, "question": "What is 2 + 2?", "answer": "4", "damage": 10, "experience_reward": 10},
    {"name": "Bug2", "health": 100, "question": "What is the capital of France?", "answer": "Paris", "damage": 20, "experience_reward": 15}
]

# Potions data
potions = [
    {"name": "Health Potion", "restore": 30}
]

def draw_text(screen, text, font, color, pos):
    render = font.render(text, True, color)
    rect = render.get_rect(center=pos)
    screen.blit(render, rect)

def show_inventory(screen, font):
    y_offset = 100
    for item in player["inventory"]:
        draw_text(screen, item["name"], font, WHITE, (WIDTH // 2, y_offset))
        y_offset += 40

def use_potion():
    # Restore health by potion's restore value
    if len(player["inventory"]) > 0:
        potion = player["inventory"].pop()  # Use the last potion
        player["health"] += potion["restore"]
        if player["health"] > 100:
            player["health"] = 100  # Cap health at 100

def run_game_world(screen):
    font = pygame.font.SysFont("arial", 32)
    clock = pygame.time.Clock()

    current_enemy = 0  # Start with the first enemy
    running = True
    while running:
        screen.fill((20, 30, 40))

        # Check if there is an enemy to defeat
        if current_enemy < len(enemies):
            enemy = enemies[current_enemy]
            draw_text(screen, f"Defeat {enemy['name']}", font, WHITE, (WIDTH // 2, HEIGHT // 2 - 50))
            draw_text(screen, f"Enemy Health: {enemy['health']}", font, WHITE, (WIDTH // 2, HEIGHT // 2 - 10))
            draw_text(screen, f"Question: {enemy['question']}", font, WHITE, (WIDTH // 2, HEIGHT // 2 + 30))

            # Display player health
            draw_text(screen, f"Your Health: {player['health']}", font, WHITE, (WIDTH // 2, HEIGHT // 2 + 70))

            # Display inventory
            draw_text(screen, f"Press 'I' for Inventory", font, WHITE, (WIDTH // 2, HEIGHT - 40))

        else:
            draw_text(screen, "All enemies defeated! Press ESC to return to menu.", font, WHITE, (WIDTH // 2, HEIGHT // 2 - 50))

        # Check if player has lost
        if player['health'] <= 0:
            draw_text(screen, "You have been defeated! Press ESC to return to menu.", font, WHITE, (WIDTH // 2, HEIGHT // 2 - 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"
                elif event.key == pygame.K_RETURN:  # Press 'Enter' to answer the question
                    # Simulate an input question (in real scenarios, we should use pygame's text input)
                    answer = input(f"Answer the question: {enemies[current_enemy]['question']} ")

                    if answer == enemies[current_enemy]["answer"]:
                        # Correct answer, defeat the enemy and reward experience
                        enemies[current_enemy]["health"] = 0  # Defeat the enemy
                        player["experience"] += enemies[current_enemy]["experience_reward"]

                        # Level up after reaching a certain experience threshold
                        if player["experience"] >= 30 * player["level"]:
                            player["level"] += 1
                            player["health"] += 20  # Increase health on level up

                        # Optionally, add a potion to the inventory
                        if random.random() < 0.5:  # 50% chance to drop a health potion
                            player["inventory"].append(potions[0])  # Add a health potion

                        current_enemy += 1  # Move to the next enemy

                    else:
                        # Incorrect answer, damage player
                        player['health'] -= enemies[current_enemy]["damage"]
                        draw_text(screen, "Incorrect answer! You took damage.", font, WHITE, (WIDTH // 2, HEIGHT // 2 + 70))

                elif event.key == pygame.K_i:  # Show inventory when 'I' is pressed
                    show_inventory(screen, font)

                elif event.key == pygame.K_u:  # Use potion when 'U' is pressed
                    use_potion()

        pygame.display.flip()
        clock.tick(60)
