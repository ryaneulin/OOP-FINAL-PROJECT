import pygame
from player import Player  # Assuming you have a Player class in player.py
from enemy import Enemy    # Assuming you have an Enemy class in enemy.py

# Initialize pygame
pygame.init()

# Screen setup
w_width, w_height = 1280, 720
BG_color = (50, 50, 50)  # Background color
screen = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption("Game World")

# Font setup (for UI or messages)
font = pygame.font.Font(None, 36)

class GameWorld:
    def __init__(self):
        print("Initializing GameWorld...")
        # Player setup
        self.player = Player(100, 300, ["my_game\\assets\\rightplayer\\0 (3).png", "my_game\\assets\\rightplayer\\1 (3).png", "my_game\\assets\\rightplayer\\2 (3).png", "my_game\\assets\\rightplayer\\3 (3).png"],
                             ["my_game\\assets\\leftplayer\\0 (2).png", "my_game\\assets\\leftplayer\\1 (2).png", "my_game\\assets\\leftplayer\\2 (2).png", "my_game\\assets\\leftplayer\\3 (2).png"],
                             ["my_game\\assets\\downplayer\\0 (1).png", "my_game\\assets\\downplayer\\1 (1).png", "my_game\\assets\\downplayer\\2 (1).png", "my_game\\assets\\downplayer\\3 (1).png"],
                             ["my_game\\assets\\upplayer\\0.png", "my_game\\assets\\upplayer\\1.png", "my_game\\assets\\upplayer\\2.png", "my_game\\assets\\upplayer\\3.png"])

        # Enemy setup
        self.enemy = Enemy(500, 300, [
            "my_game\\assets\\enemy1\\enemy1.png", 
            "my_game\\assets\\enemy1\\enemy2.png", 
            "my_game\\assets\\enemy1\\enemy3.png", 
            "my_game\\assets\\enemy1\\enemy4.png"  # Corrected path
        ])
        
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player, self.enemy)

    def spawn_player(self):
        print("Spawning player at position (100, 300)...")
        self.player.rect.topleft = (100, 300)
        self.player.velocity = pygame.math.Vector2(0, 0)

    def spawn_enemy(self):
        print("Spawning enemy at position (500, 300)...")
        self.enemy.rect.topleft = (500, 300)

    def draw(self):
        screen.fill(BG_color)
        self.sprites.update()
        self.sprites.draw(screen)

    def game_loop(self):
        print("Starting game loop...")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_w:
                        self.player.velocity.y = -self.player.speed
                    elif event.key == pygame.K_s:
                        self.player.velocity.y = self.player.speed
                    elif event.key == pygame.K_a:
                        self.player.velocity.x = -self.player.speed
                    elif event.key == pygame.K_d:
                        self.player.velocity.x = self.player.speed

                elif event.type == pygame.KEYUP:
                    if event.key in [pygame.K_w, pygame.K_s]:
                        self.player.velocity.y = 0
                    if event.key in [pygame.K_a, pygame.K_d]:
                        self.player.velocity.x = 0

            self.draw()
            pygame.display.flip()
            pygame.time.delay(30)

        pygame.quit()

def enter_game_world(screen):
    print("Entering game world...")
    game_world = GameWorld()
    game_world.spawn_player()
    game_world.spawn_enemy()
    game_world.game_loop()
