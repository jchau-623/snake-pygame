import pygame
import sys

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Your Game")

# Set up game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic here
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Collision detection
    if player_rect.colliderect(obstacle_rect):
        print("Collision!")


    # Draw to the screen
    screen.fill((255, 255, 255))  # Fill screen with white color

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)  # 60 frames per second

pygame.quit()
sys.exit()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            # Handle spacebar press
            pass

player_image = pygame.image.load("assets/player.png")
player_rect = player_image.get_rect()

# Display image on the screen
screen.blit(player_image, player_rect)

pygame.mixer.init()
gunshot_sound = pygame.mixer.Sound("assets/gunshot.wav")

# Play the sound
gunshot_sound.play()