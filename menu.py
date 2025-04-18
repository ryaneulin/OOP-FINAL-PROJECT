import pygame

white = (255, 255, 255)
black = (0, 0, 0)
button_color = (100, 100, 255)
w_width, w_height = 800, 600

def draw_text(screen, text, font, color, pos):
    render = font.render(text, True, color)
    rect = render.get_rect(center=pos)
    screen.blit(render, rect)

def white_fade_in(screen, duration=1000):
    clock = pygame.time.Clock()
    fade_surface = pygame.Surface((w_width, w_height))
    fade_surface.fill(white)
    alpha = 255
    fade_speed = 255 / (duration / 16)

    while alpha > 0:
        fade_surface.set_alpha(int(alpha))
        screen.blit(fade_surface, (0, 0))
        pygame.display.update()
        clock.tick(60)
        alpha -= fade_speed

def show_menu(screen):
    font = pygame.font.SysFont("arial", 40)
    clock = pygame.time.Clock()
    button_rect = pygame.Rect(w_width // 2 - 100, w_height // 2 - 30, 200, 60)

    while True:
        screen.fill(black)
        draw_text(screen, "Main Menu", font, white, (w_width // 2, w_height // 2 - 100))

        pygame.draw.rect(screen, button_color, button_rect)
        draw_text(screen, "Start Game", font, white, button_rect.center)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    white_fade_in(screen)
                    return "dialogue"
                
        pygame.display.flip()
        clock.tick(60)
