import random  # used to generate a random boost during the gameplay
from paddle import *  # necessary file
from bricks import *  # necessary file
from boosts import *  # necessary file
from ball import *  # necessary file
from heart import *  # necessary file

# Initialize Pygame
pygame.init()

# Set up the game window, backgrounds, fonts
start_image = pygame.image.load("images/start-image.jpg")  # opening image
start_image = pygame.transform.scale(start_image, (window_width, window_height))  # opening image scaling
window = pygame.display.set_mode((window_width, window_height))  # setting game window dimensions
background = pygame.image.load("images/bg.jpg")  # game background image
background = pygame.transform.scale(background, (window_width, window_height))    # game background image scaling
pygame.display.set_caption("SMASH IT")  # setting game name on the title bar
icon_image = pygame.image.load("images/icon.jpg")  # Game icon
pygame.display.set_icon(icon_image)  # setting the application icon shown on the left of the title bar
score_font = pygame.font.Font(None, 40)  # setting score font and score font size
score_color = (0, 0, 0)  # Black color
bricks_destroyed_font = pygame.font.Font(None, 30)  # setting destroyed bricks number font and its size
bricks_destroyed_color = (0, 0, 0)  # Black color

# Game music
pygame.mixer.music.load("sounds/game-music.mp3")   # in-game music
pygame.mixer.music.set_volume(0.3)   # volume setting (30%)
pygame.mixer.music.play(-1)  # Playing the music in a loop (-1 = infinite loop)

# Set up the paddle
paddle = Paddle()

# Set up the ball
ball = Ball()

# Set up the bricks
layer1 = Layer1()
layer2 = Layer2()
layer3 = Layer3()
layer4 = Layer4()
layers = [layer1, layer2, layer3, layer4]

# Set up the hearts
hearts = Hearts(lives)
heart_destroyed_sound = pygame.mixer.Sound("sounds/blood-pop.wav")   # losing a life(heart) sound effect
heart_destroyed_sound.set_volume(0.3)  # sets volume to 30%

# Set up the game clock
clock = pygame.time.Clock()

# Setting the Game ending
winning_image = pygame.image.load("images/winning_image2.jpg")   # winning image
winning_image = pygame.transform.scale(winning_image, (window_width, window_height))   # winning image scaling
losing_image = pygame.image.load("images/you-lost.jpg")   # losing image
losing_image = pygame.transform.scale(losing_image, (window_width, window_height))   # losing image scaling
winning_sound = pygame.mixer.Sound("sounds/winning-sound.wav")   # winning sound effect
winning_sound.set_volume(0.4)  # sets volume to 40%
losing_sound = pygame.mixer.Sound("sounds/losing-sound.wav")   # losing sound effect
losing_sound.set_volume(0.4)  # sets volume to 40%

# Setting up Boosts
paddle_increase = PaddleWidthIncrease()
paddle_decrease = PaddleWidthDecrease()
life_increase = LifeIncreaseBoost()
life_decrease = LifeDecreaseBoost()
speed_increase = BallSpeedIncrease()
speed_decrease = BallSpeedDecrease()
boost_objs = [paddle_increase, paddle_decrease, life_increase, life_decrease, speed_increase, speed_decrease]
active_boost = None  # used to control boosts activation

# Game loop
running = True  # while true the game keeps running
show_start_image = True   # while true the opening image stays on

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:  # quitting the game button
            running = False  # results in stopping the game
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:  # pressing the space button removes the opening image and leads to the gameplay
                show_start_image = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    paddle.move(keys)

    # Paddle and ball collision
    if ball.check_collision(paddle.rect):
        ball.reverse_direction()

    # Brick and ball collision
    for layer in layers:
        score += layer.check_collision(ball)

    if active_boost is None and score in [5, 15, 25]:  # boost activation determinants
        active_boost = random.choice(boost_objs)  # random boost activated

    # Game over conditions
    if score == brick_rows*brick_cols:  # if all the bricks are destroyed
        pygame.mixer.music.stop()  # Stop playing the background music
        winning_sound.play()   # plays the game over sound
        window.blit(winning_image, (0, 0))  # Display game over image
        pygame.display.update()
        pygame.time.wait(3000)  # Wait for a few seconds before quitting (in milliseconds) = 3 seconds
        running = False  # stops the game

    elif ball.check_game_over(window_height):  # ball fell off the screen(resets the ball, decrements lives and deactivates boosts)
        ball.speed_x = ball_speed_x  # resets ball x-speed
        ball.speed_y = ball_speed_y  # resets ball y-speed
        default_size()  # resets paddle size variables(height, width)
        paddle.image = pygame.transform.scale(paddle.image, (paddle_width, paddle_height))  # displays the paddle with its default size
        lives -= 1  # lives decrement
        heart_destroyed_sound.play()  # playing destroyed heart sound effect
        hearts.lose_life()  # removing one heart from the display
        if settings.get_lives() <= 0:  # losing the game due to losing all the lives
            # Display game over image
            pygame.mixer.music.stop()  # stops game music
            losing_sound.play()  # plays losing the game sound effect
            window.blit(losing_image, (0, 0))  # displays the losing image
            bricks_destroyed = bricks_destroyed_font.render(f"You destroyed: ({score}) bricks out of 32", True, bricks_destroyed_color)  # displays the score(number of bricks destroyed)
            bricks_destroyed_rect = bricks_destroyed.get_rect()  # "rect" is a rectangle object that represents the bounding box of the score text surface
            bricks_destroyed_rect.bottomright = (window_width // 2 + 165, window_height - 60)  # specifies the coordinates of the rectangle, to position the score in a specified location
            window.blit(bricks_destroyed, bricks_destroyed_rect)  # displays the text
            pygame.display.update()  # updates the display
            pygame.time.wait(3000)  # waits 3 seconds
            running = False  # stops the game

        else:  # if the player didn't win nor lose resets the ball and carry on
            ball.reset()  # resets the ball

    # Activating boosts
    if active_boost is not None and isinstance(active_boost, PaddleWidthIncrease) or isinstance(active_boost, PaddleWidthDecrease):
        active_boost.move()  # one boost starts moving(fall from the top of the screen)
        active_boost.apply_effect(paddle)  # if the paddle collides with the boost the boosts effect applies
        if active_boost.rect.top >= window_height:  # removes the boost if it fell off the screen without colliding with the paddle
            active_boost = None  # updates the boosts activation controller

    elif active_boost is not None and isinstance(active_boost, LifeIncreaseBoost) or isinstance(active_boost, LifeDecreaseBoost):
        active_boost.move()  # explained previously
        active_boost.apply_effect(hearts, paddle)  # explained previously
        if active_boost.rect.top >= window_height:  # explained previously
            active_boost = None  # explained previously

    elif active_boost is not None and isinstance(active_boost, BallSpeedIncrease) or isinstance(active_boost, BallSpeedDecrease):
        active_boost.move()  # explained previously
        active_boost.apply_effect(ball, paddle)  # explained previously
        if active_boost.rect.top >= window_height:  # explained previously
            active_boost = None  # explained previously

    # Drawing the game objects
    if show_start_image:  # while the space key still not pressed
        window.blit(start_image, (0, 0))  # displays the start image
    else:  # the space key got pressed so the opening image go away and the game starts
        window.blit(background, (0, 0))  # displays the game background

        # Ball movement
        ball.move(paddle)  # now the ball finally starts moving

        paddle.draw(window)  # displays the paddle

        ball.draw(window)  # displays the ball

        layer1.draw(window)  # displays the first layer(from top)

        layer2.draw(window)  # displays the second layer

        layer3.draw(window)  # displays the third layer

        layer4.draw(window)  # displays the fourth layer(first from bottom)

        hearts.draw(window)  # displays the hearts

        score_text = score_font.render(f"Score: {score}", True, score_color)  # displays the score(number of bricks destroyed)
        score_text_rect = score_text.get_rect()  # explained previously
        score_text_rect.bottomright = (window_width - 10, window_height - 10)  # explained previously
        window.blit(score_text, score_text_rect)  # displays the score on the game background

        if active_boost is not None:  # if there is an activated boost
            active_boost.draw(window)  # displays the boost image

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)


# Game Over
pygame.quit()
