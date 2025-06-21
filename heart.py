import pygame  # necessary files
from settings import*  # necessary files
import settings  # necessary files


class Heart:
    def __init__(self, image_path, x, y):  # heart object constructor
        self.image = pygame.image.load(image_path)  # sets the heart image based on its path
        self.image = pygame.transform.scale(self.image, (30, 30))  # scales the heart image
        self.rect = self.image.get_rect()  # previously explained
        self.rect.x = x  # previously explained
        self.rect.y = y  # previously explained

    def draw(self, window):  # used to display the heart image
        window.blit(self.image, self.rect)


class Hearts:
    def __init__(self, lives):  # hearts object constructor
        self.lives = lives  # sets the hearts lives
        self.heart_images = ["images/heart.png"] * lives  # sets the hearts image for each heart(hearts number = lives)
        self.hearts = []  # creates a list of heart objects

        for i in range(lives):
            x = 10 + i * (30 + 5)  # adjusts the spacing between hearts
            y = window_height - 40  # adjusts the y-coordinate of the hearts
            heart = Heart(self.heart_images[i], x, y)  # creating heart objects
            self.hearts.append(heart)  # adding the created heart objects to the list

    def add_life(self):  # used by a boost to create a new heart object and increment lives
        settings.increment_lives()  # increments lives
        self.lives += 1  # inner use
        x = 10 + (self.lives-1) * (30 + 5)  # adjusts the spacing between hearts
        y = window_height - 40  # adjusts the y-coordinate of the hearts
        heart = Heart("images/heart.png", x, y)  # creates the new heart
        self.hearts.append(heart)  # adds the new heart to the hearts list

    def lose_life(self):  # used by a boost to destroy a heart object and decrement lives
        if self.lives > 0:  # checks whether the decrement of lives the boost caused ended the players lives or not
            self.hearts.pop()  # destroys one of the hearts
            settings.decrement_lives()  # decrements lives
            self.lives -= 1  # inner use

    def draw(self, window):  # used to draw the hearts in the list
        for heart in self.hearts:
            heart.draw(window)
