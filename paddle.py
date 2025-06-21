import pygame  # necessary files
from pygame.locals import *  # necessary files
import settings  # necessary files
from settings import *  # necessary files


class Paddle:
    def __init__(self):  # paddle object constructor
        self.width = paddle_width  # setting paddles width and height
        self.height = paddle_height
        self.image = pygame.image.load("images/paddle.png")  # sets the paddle image
        self.image = pygame.transform.scale(self.image, (settings.return_width(), settings.return_height()))  # scales the paddle image
        self.rect = self.image.get_rect()  # creates a bounding rectangle around the paddle image
        self.x = window_width // 2 - self.width // 2  # previously explained
        self.y = window_height - 100  # previously explained
        self.speed = paddle_speed  # setting paddles speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # initializes the paddles rectangle using the provided position and size values

    def move(self, keys):  # paddles movement
        if keys[K_LEFT] and self.rect.left > 0:  # moving the paddle using the left key and keeping it in the window frames
            self.rect.left -= self.speed  # movement to the left
        if keys[K_RIGHT] and self.rect.right < window_width and return_width() == 120:  # moving the paddle using the right key and keeping it in the window frames
            self.rect.right += self.speed  # movement to the right
        elif keys[K_RIGHT] and self.rect.right < window_width-40 and return_width() == 160:  # so the paddle doesn't go off-screen when its size is increased
            self.rect.right += self.speed  # movement to the right
        elif keys[K_RIGHT] and self.rect.right < window_width+40 and return_width() == 80:  # so the paddle can reach the side when its size is decreased
            self.rect.right += self.speed  # movement to the right

    def draw(self, window):  # used to display the paddle
        window.blit(self.image, self.rect)
