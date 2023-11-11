import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((600, 150))
pygame.display.set_caption("Dinosaur Game")

# Load the images
dino_img = pygame.image.load("dino.png")
cactus_img = pygame.image.load("cactus.png")

# Set up the dino and cactus
dino_x = 50
dino_y = 100
cactus_x = 600
cactus_y = 100
cactus_speed = 5

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the game variables
score = 0
game_over = False

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino_y -= 30

    # Update the cactus position
    cactus_x -= cactus_speed

    # Check for collision
    if cactus_x <= dino_x + 50 and cactus_x + 50 >= dino_x:
        if dino_y + 50 >= cactus_y:
            game_over = True

    # Update the score
    score += 1

    # Draw the background
    screen.fill((255, 255, 255))

    # Draw the dino
    screen.blit(dino_img, (dino_x, dino_y))

    # Draw the cactus
    screen.blit(cactus_img, (cactus_x, cactus_y))

    # Draw the score
    score_text = font.render(str(score), True, (0, 0, 0))
    screen.blit(score_text, (550, 50))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
