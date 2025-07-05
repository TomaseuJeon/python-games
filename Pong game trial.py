import pygame
import random
import time


# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 7
PADDLE_SPEED = 6
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Ball properties
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_pos_x = float(ball.x)
ball_pos_y = float(ball.y)
ball_speed_x = BALL_SPEED * random.choice((-1, 1))
ball_speed_y = BALL_SPEED * random.choice((-1, 1))

# Paddles
paddle_a = pygame.Rect(50, HEIGHT // 2 - 60, 10, 120)
paddle_b = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 60, 10, 120)

# Scores
score_a = 0
score_b = 0

# Fonts
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= PADDLE_SPEED
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += PADDLE_SPEED
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += PADDLE_SPEED

    # Update ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Ball collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    # Ball out of bounds (score)
    if ball.left <= 0:
        score_b += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_pos_x = float(ball.x)
        ball_pos_y = float(ball.y)
        ball_speed_x = BALL_SPEED
        ball_speed_y = BALL_SPEED * random.choice((1, -1))
    if ball.right >= WIDTH:
        score_a += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_pos_x = float(ball.x)
        ball_pos_y = float(ball.y)
        ball_speed_x = -BALL_SPEED
        ball_speed_y = BALL_SPEED * random.choice((1, -1))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw paddles, ball, and score
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)
    score_display = font.render(f"{score_a} - {score_b}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 30, 20))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()