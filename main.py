import pygame
import sys
import random

pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Your Game")

# Set up game objects
player_image = pygame.Surface((20, 20))  # Snake segment size
player_image.fill((0, 255, 0))  # Green color for the snake
player_rect = player_image.get_rect()

# Set up sounds
pygame.mixer.init()
crash_sound = pygame.mixer.Sound("assets/crash.mp3")

# Set up fonts for text rendering
font = pygame.font.Font(None, 36)
text_color = (255, 0, 0)  # Red color for the text

# Initialize snake body and position
snake_body = [player_rect.copy()]  # Start with a single rectangle for the head
player_rect.topleft = (width // 2, height // 2)  # Set initial position of the snake

# Initialize food object
food_image = pygame.Surface((20, 20))  # Example food image
food_image.fill((255, 0, 0))  # Red color for the food
food_rect = food_image.get_rect()
food_rect.x = random.randint(0, width - food_rect.width)
food_rect.y = random.randint(0, height - food_rect.height)

# Set up retry button
button_font = pygame.font.Font(None, 36)
button_text = button_font.render("Retry", True, (0, 0, 0))  # Text for the button
button_rect = button_text.get_rect(center=(width // 2, height // 2 + 50))  # Position of the button

# Set up game loop
clock = pygame.time.Clock()
running = True
speed = 10  # Base speed
x_change, y_change = speed, 0  # Initial movement direction

game_over = False  # Initially, the game is not over

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change != speed:  # Check if not moving right
                x_change = -speed
                y_change = 0
            elif event.key == pygame.K_RIGHT and x_change != -speed:  # Check if not moving left
                x_change = speed
                y_change = 0
            elif event.key == pygame.K_UP and y_change != speed:  # Check if not moving down
                x_change = 0
                y_change = -speed
            elif event.key == pygame.K_DOWN and y_change != -speed:  # Check if not moving up
                x_change = 0
                y_change = speed

    # Update snake position based on direction variables
    player_rect.move_ip(x_change, y_change)

    # Check if the snake collides with itself
    for segment in snake_body[1:]:
        if player_rect.colliderect(segment):
            print("Game Over - Snake collided with itself")
            crash_sound.play()
            game_over = True
            break  # Exit the loop if collision detected


    # Check if the snake hits the screen boundaries (corners)
    if (player_rect.left <= 0 or player_rect.right >= width or
            player_rect.top <= 0 or player_rect.bottom >= height):
        print("Game Over")
        crash_sound.play()
        game_over = True

    if not game_over:  # Only execute game logic if the game is not over
        if player_rect.colliderect(food_rect):
            # Increase snake length
            snake_body.append(player_rect.copy())
            # Generate new food at random position
            food_rect.x = random.randint(0, width - food_rect.width)
            food_rect.y = random.randint(0, height - food_rect.height)
            # Increase speed every time the snake eats food
            speed += 1  # or any other value that suits your game

        # Update snake body
        snake_body.insert(0, player_rect.copy())  # Add the new head to the beginning of the list
        snake_body = snake_body[:len(snake_body) - 1]  # Remove the last segment (tail)

    # Draw to the screen
    screen.fill((255, 255, 255))

    # Draw food
    screen.blit(food_image, food_rect)

    # Draw snake body
    for segment in snake_body:
        screen.blit(player_image, segment)

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(10)  # Slowed down for better visibility

    if game_over:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((255, 255, 255))  # Clear the screen
            game_over_text = font.render("Game Over", True, text_color)
            text_rect = game_over_text.get_rect(center=(width // 2, height // 2))
            screen.blit(game_over_text, text_rect)

            # Draw the retry button
            pygame.draw.rect(screen, (200, 200, 200), button_rect)
            screen.blit(button_text, button_rect)

            pygame.display.flip()  # Update the display to show "Game Over"

            # make differnt folders for code
            # fix error for everytime the snake turns after eating one fruit it ends game
            # make retry button work