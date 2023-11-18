import pygame
import time
import random

pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

# Snake initial position and properties
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1

# Initial position of the snake
snake_head = [width // 2, height // 2]
snake_list.append(snake_head)

# Initial direction
direction = "RIGHT"
change_to = direction

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Function to display the score
def Your_score(score):
    font = pygame.font.SysFont(None, 35)
    score_text = font.render("Your Score: " + str(score), True, white)
    window.blit(score_text, [0, 0])

# Function to run the game
def gameLoop():
    # Global variables
    global direction
    global change_to
    global snake_length

    # Initial game conditions
    game_over = False
    game_close = False

    # Initial position of the food
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Main game loop
    while not game_over:

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not direction == "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and not direction == "LEFT":
                    change_to = "RIGHT"
                elif event.key == pygame.K_UP and not direction == "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and not direction == "UP":
                    change_to = "DOWN"

        # Update direction
        direction = change_to

        # Move the snake
        if direction == "RIGHT":
            snake_head[0] += snake_block
        elif direction == "LEFT":
            snake_head[0] -= snake_block
        elif direction == "UP":
            snake_head[1] -= snake_block
        elif direction == "DOWN":
            snake_head[1] += snake_block

        # Game over if snake hits the boundaries
        if (
            snake_head[0] >= width
            or snake_head[0] < 0
            or snake_head[1] >= height
            or snake_head[1] < 0
        ):
            game_close = True

        # Update snake length
        snake_list.append(list(snake_head))
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Game over if snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake and the food
        window.fill(black)
        our_snake(snake_block, snake_list)
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
        Your_score(snake_length - 1)

        # Update the display
        pygame.display.update()

        # Generate new food if the snake eats it
        if snake_head[0] == foodx and snake_head[1] == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        # Set the game speed
        pygame.time.Clock().tick(snake_speed)

        # Game over screen
        while game_close:
            window.fill(black)
            font = pygame.font.SysFont(None, 70)
            message = font.render("Game Over", True, red)
            window.blit(message, [width / 6, height / 3])
            Your_score(snake_length - 1)
            pygame.display.update()

            # Ask the user if they want to play again
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

    pygame.quit()
    quit()

# Run the game
gameLoop()
