import pygame  # necessary files
from settings import *  # necessary files


class Brick:
    def __init__(self, x, y, image_path, hits_required, sound_path):  # brick object constructor
        self.rect = pygame.Rect(x, y, brick_width, brick_height)  # previously explained
        self.image = pygame.image.load(image_path)  # previously explained
        self.image = pygame.transform.scale(self.image, (brick_width, brick_height))  # previously explained
        self.hits_required = hits_required  # sets the hits required to destroy each brick
        self.sound_path = pygame.mixer.Sound(sound_path)   # sets each of the bricklayers sound effects

    def check_collision(self, ball):  # used to check for collisions with the ball
        if self.rect.colliderect(ball.rect):
            self.sound_path.play()  # plays the ball-brick hit sound effect
            ball.reverse_direction()  # reverse the ball direction
            self.hits_required -= 1  # each hit decrements the amount of hits a brick can take before getting destroyed
            if self.hits_required <= 0:  # checks whether the brick reached the hit-limit
                return True  # indicates that the brick should be removed
        return False  # indicates that the brick wasn't hit by the ball

    def draw(self, window):  # used to display the image of the brick
        window.blit(self.image, self.rect)


class Layer1:
    def __init__(self, image_path="images/emerald-bricks.png", hits_required=4):  # layer 1 object constructor
        self.image_path = image_path   # sets the layers bricks image based on image_path
        self.hits_required = hits_required  # sets the hits required to destroy each brick of this layer
        self.bricks = []  # creates a list of layer1 objects(bricks)
        self.sound_path = pygame.mixer.Sound("sounds/gem-hit.wav")  # layer1-ball hit sound effect
        for col in range(brick_cols):  # creating,positioning each brick and appending it to the bricks list
            brick_x = col * (brick_width + brick_spacing_x)
            brick_y = 5
            brick = Brick(brick_x, brick_y, self.image_path, self.hits_required, self.sound_path)
            self.bricks.append(brick)

    def check_collision(self, ball):  # checks for collision with the ball
        score = 0  # sets the score
        for brick in self.bricks:  # checking for collision with the ball for all the bricks in the layer
            if brick.check_collision(ball):
                self.bricks.remove(brick)  # removing the bricks that reached the hit-limit
                score += 1  # incrementing the score whenever a brick is destroyed
        return score

    def draw(self, window):  # used to draw the bricks in the list
        for brick in self.bricks:
            brick.draw(window)


class Layer2:
    def __init__(self, image_path="images/goldBrick.png", hits_required=3):  # layer 2 object constructor
        self.image_path = image_path  # previously explained
        self.hits_required = hits_required  # previously explained
        self.bricks = []  # previously explained
        self.sound_path = pygame.mixer.Sound("sounds/gold-hit.wav")  # layer2-ball hit sound effect
        for col in range(brick_cols):  # previously explained
            brick_x = col * (brick_width + brick_spacing_x)
            brick_y = 55
            brick = Brick(brick_x, brick_y, image_path, 3, self.sound_path)
            self.bricks.append(brick)

    def check_collision(self, ball):  # previously explained
        score = 0
        for brick in self.bricks:
            if brick.check_collision(ball):
                self.bricks.remove(brick)
                score += 1
        return score

    def draw(self, window):  # previously explained
        for brick in self.bricks:
            brick.draw(window)


class Layer3:
    def __init__(self, image_path="images/stoneBrick.png", hits_required=2):  # layer 3 object constructor
        self.image_path = image_path  # previously explained
        self.hits_required = hits_required  # previously explained
        self.bricks = []  # previously explained
        self.sound_path = pygame.mixer.Sound("sounds/stone-hit.wav")  # layer3-ball hit sound effect
        for col in range(brick_cols):  # previously explained
            brick_x = col * (brick_width + brick_spacing_x)
            brick_y = 105
            brick = Brick(brick_x, brick_y, image_path, 2, self.sound_path)
            self.bricks.append(brick)

    def check_collision(self, ball):  # previously explained
        score = 0
        for brick in self.bricks:
            if brick.check_collision(ball):
                self.bricks.remove(brick)
                score += 1
        return score

    def draw(self, window):  # previously explained
        for brick in self.bricks:
            brick.draw(window)


class Layer4:
    def __init__(self, image_path="images/woodBrick.png", hits_required=1):  # layer 4 object constructor
        self.image_path = image_path  # previously explained
        self.hits_required = hits_required  # previously explained
        self.bricks = []  # previously explained
        self.sound_path = pygame.mixer.Sound("sounds/wood-hit.wav")  # layer4-ball hit sound effect
        for col in range(brick_cols):  # previously explained
            brick_x = col * (brick_width + brick_spacing_x)
            brick_y = 155
            brick = Brick(brick_x, brick_y, image_path, 1, self.sound_path)
            self.bricks.append(brick)

    def check_collision(self, ball):  # previously explained
        score = 0
        for brick in self.bricks:
            if brick.check_collision(ball):
                self.bricks.remove(brick)
                score += 1
        return score

    def draw(self, window):  # previously explained
        for brick in self.bricks:
            brick.draw(window)
