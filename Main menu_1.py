import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 72)

# Create buttons
start_button = pygame.Rect(300, 200, 200, 50)
settings_button = pygame.Rect(300, 300, 200, 50)
exit_button = pygame.Rect(300, 400, 200, 50)

game_title = title_font.render("CLICKER", True, BLACK)
title_rect = game_title.get_rect(center=(WIDTH // 2, 100))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    print("HEY THIS WORKS!")
                elif exit_button.collidepoint(mouse_pos):
                    running = False

    # Clear the screen
    SCREEN.fill(WHITE)

    # Draw buttons
    pygame.draw.rect(SCREEN, BLACK, start_button)
    pygame.draw.rect(SCREEN, BLACK, settings_button)
    pygame.draw.rect(SCREEN, BLACK, exit_button)

    # Add text to buttons
    start_text = font.render("Start", True, WHITE)
    settings_text = font.render("Settings", True, WHITE)
    exit_text = font.render("Exit", True, WHITE)

    SCREEN.blit(start_text, (370, 210))
    SCREEN.blit(settings_text, (350, 310))
    SCREEN.blit(exit_text, (370, 410))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()