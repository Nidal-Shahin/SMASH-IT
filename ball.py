import pygame  # necessary files
from settings import *  # necessary files


class Ball:
    def __init__(self):  # ball object constructor
        self.x = window_width // 2  # both self.x and self.y represent the coordinates of an object's position on the screen
        self.y = window_height // 2
        self.speed_x = ball_speed_x  # setting x-speed of the ball
        self.speed_y = ball_speed_y  # setting y-speed of the ball
        self.image = pygame.image.load("images/ball.png")  # setting the ball image
        self.image = pygame.transform.scale(self.image, (30, 30))  # scaling the ball image
        self.rect = self.image.get_rect(center=(self.x, self.y))  # used to set the center coordinates of the rectangle

    def move(self, paddle):  # ball movement function
        window_side_hit_sound = pygame.mixer.Sound("sounds/sides-hit.wav")   # ball hitting the sides and the top of the window sound effect
        window_side_hit_sound.set_volume(0.2)  # sets volume to 20%
        paddle_hit_sound = pygame.mixer.Sound("sounds/paddle-hit.wav")   # ball hitting the paddle sound effect
        paddle_hit_sound.set_volume(0.3)  # sets volume to 30%
        self.rect.x += self.speed_x  # both rect.x and rect.y are responsible for updating the ball's position based on its current speed in each frame of the game loop
        self.rect.y += self.speed_y
        if self.rect.colliderect(paddle.rect):  # checks for collision with the paddle
            paddle_hit_sound.play()  # playing the ball-paddle hit sound effect
            self.rect.bottom = paddle.rect.top  # adjusting the position of the ball after its collision with the paddle
            self.speed_y *= -1  # changes the direction of the ball y-movement to bounce off the paddle
        if self.rect.left <= 0 or self.rect.right >= window_width:  # making sure that the ball remains inside the window frames by bouncing off the sides
            window_side_hit_sound.play()  # plays the ball-side hit sound effect
            self.speed_x *= -1  # changes the direction of the ball x-movement to bounce off the sides
        if self.rect.top <= 0:  # similar to the previous conditional statement(by bouncing off the top of the screen)
            window_side_hit_sound.play()  # plays the ball-top hit sound effect
            self.speed_y *= -1  # changes the direction of the ball y-movement to bounce off the top

    def check_collision(self, obj):  # checks for collision with the bricks
        return self.rect.colliderect(obj)

    def reverse_direction(self):  # used to reverse the direction of the balls y-movement
        self.speed_y *= -1

    def check_game_over(self, window_height):  # checks whether the ball fell off the screen or not
        return self.rect.bottom >= window_height

    def reset(self):  # resets the ball after falling off(if there are lives remaining)
        self.rect.x = window_width // 2  # positioning the ball at the center again
        self.rect.y = window_height // 2  # same usage
        self.speed_x = ball_speed_x  # Reset horizontal speed to default
        self.speed_y = ball_speed_y  # Reset vertical speed to default

    def draw(self, window):  # used to display the balls image
        window.blit(self.image, self.rect)
