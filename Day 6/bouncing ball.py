import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Elastic Ball Animation")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_color = RED
ball_x = WIDTH // 2
ball_y = ball_radius
ball_speed_y = 0
gravity = 0.5
elasticity = 0.8

clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ball physics
    ball_speed_y += gravity
    ball_y += ball_speed_y

    # Collision with ground
    if ball_y + ball_radius > HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_speed_y = -ball_speed_y * elasticity

    # Clear screen
    screen.fill(WHITE)

    # Draw ball
    pygame.draw.circle(screen, ball_color, (ball_x, int(ball_y)), ball_radius)

    # Update the display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
