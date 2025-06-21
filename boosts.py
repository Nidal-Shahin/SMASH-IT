import pygame  # necessary files
import settings  # necessary files
from settings import*  # necessary files


class Boosts:
    def __init__(self, imagePath):  # boosts object constructor
        self.x = window_width // 2  # position at the middle of the screen
        self.y = 0
        self.image = pygame.image.load(imagePath)  # setting each boost image based on its path that will be passed by the boosts constructors
        self.image = pygame.transform.scale(self.image, (boost_width, boost_height))  # scaling each image
        self.speed_x = boost_speed_x  # both speed_x and speed_y used to set the speed of the fallen boost
        self.speed_y = boost_speed_y
        self.rect = self.image.get_rect(center=(self.x, self.y))  # previously explained
        self.rect.top = 0  # position at the top of the screen

    def move(self):  # boost movement
        self.rect.y += self.speed_y  # updates the boost position to make it fall

    def draw(self, window):  # used to display the image of the boost
        window.blit(self.image, self.rect)


class PaddleWidthIncrease(Boosts):
    def __init__(self):  # PaddleWidthIncrease object constructor
        super().__init__("images/sizeIncrease.png")  # passing the image path to the base class constructor

    def apply_effect(self, paddle):  # used to apply the affect of this boost
        Collect_sound = pygame.mixer.Sound("sounds/BoostCollect.wav")  # collecting boost sound effect
        Collect_sound.set_volume(0.3)  # sets volume to 30%
        if self.rect.colliderect(paddle.rect):  # checks for collision with the paddle
            Collect_sound.play()  # plays the ball-paddle hit sound effect
            settings.increment_size()  # increments paddles width and height
            paddle.image = pygame.transform.scale(paddle.image, (settings.return_width(), settings.return_height()))  # displays the paddle after size-increase
            self.rect.y = window_height  # moves the boost off-screen
            del self  # deletes the object post-collision
        elif self.rect.top >= window_height:  # checks whether the boost fell off the screen
            del self  # deletes the object post-falling off

    def check_collision(self, obj):  # checks for collision with the paddle
        return self.rect.colliderect(obj)


class PaddleWidthDecrease(Boosts):
    def __init__(self):  # previously explained
        super().__init__("images/sizeDecrease.png")  # previously explained

    def apply_effect(self, paddle):  # previously explained
        spell_sound = pygame.mixer.Sound("sounds/spell.wav")  # previously explained
        spell_sound.set_volume(0.3)  # previously explained
        if self.rect.colliderect(paddle.rect):  # previously explained
            spell_sound.play()  # previously explained
            settings.decrement_size()  # previously explained
            paddle.image = pygame.transform.scale(paddle.image, (settings.return_width(), settings.return_height()))  # previously explained
            self.rect.y = window_height  # previously explained
            del self  # previously explained
        elif self.rect.top >= window_height:  # previously explained
            del self  # previously explained

    def check_collision(self, obj):  # previously explained
        return self.rect.colliderect(obj)


class LifeIncreaseBoost(Boosts):
    def __init__(self):  # previously explained
        super().__init__("images/heartIncrease.png")  # previously explained

    def apply_effect(self, hearts, paddle):  # previously explained
        Collect_sound = pygame.mixer.Sound("sounds/BoostCollect.wav")  # previously explained
        Collect_sound.set_volume(0.3)  # previously explained
        if self.rect.colliderect(paddle.rect):  # previously explained
            Collect_sound.play()  # previously explained
            hearts.add_life()  # displays a new heart image and increments lives
            self.rect.y = window_height  # previously explained
            del self  # previously explained
        elif self.rect.top >= window_height:  # previously explained
            del self  # previously explained

    def check_collision(self, obj):  # previously explained
        return self.rect.colliderect(obj)  # previously explained


class LifeDecreaseBoost(Boosts):
    def __init__(self):  # previously explained
        super().__init__("images/heartDecrease.png")  # previously explained

    def apply_effect(self, hearts, paddle):  # previously explained
        spell_sound = pygame.mixer.Sound("sounds/spell.wav")  # previously explained
        spell_sound.set_volume(0.3)  # previously explained
        if self.rect.colliderect(paddle.rect):  # previously explained
            spell_sound.play()  # previously explained
            hearts.lose_life()  # destroys one heart object and decrements lives
            self.rect.y = window_height  # previously explained
            del self  # previously explained
        elif self.rect.top >= window_height:  # previously explained
            del self  # previously explained

    def check_collision(self, obj):  # previously explained
        return self.rect.colliderect(obj)  # previously explained


class BallSpeedIncrease(Boosts):
    def __init__(self):  # previously explained
        super().__init__("images/speedIncrease.png")  # previously explained

    def apply_effect(self, ball, paddle):  # previously explained
        Collect_sound = pygame.mixer.Sound("sounds/BoostCollect.wav")  # previously explained
        Collect_sound.set_volume(0.3)  # previously explained
        if self.rect.colliderect(paddle.rect):  # previously explained
            Collect_sound.play()  # previously explained
            if ball.speed_x > 0 and ball.speed_y > 0:  # these 4 conditional statements checks for the balls x,y speed to apply the right effect(change)
                ball.speed_x += boost_speed_increase
                ball.speed_y += boost_speed_increase
            elif ball.speed_x < 0 < ball.speed_y:
                ball.speed_x -= boost_speed_increase
                ball.speed_y += boost_speed_increase
            elif ball.speed_x > 0 > ball.speed_y:
                ball.speed_x += boost_speed_increase
                ball.speed_y -= boost_speed_increase
            elif ball.speed_x < 0 and ball.speed_y < 0:
                ball.speed_x -= boost_speed_increase
                ball.speed_y -= boost_speed_increase
            self.rect.y = window_height  # previously explained
            del self  # previously explained
        elif self.rect.top >= window_height:  # previously explained
            del self  # previously explained

    def check_collision(self, obj):  # previously explained
        return self.rect.colliderect(obj)  # previously explained


class BallSpeedDecrease(Boosts):
    def __init__(self):  # previously explained
        super().__init__("images/speedDecrease.png")  # previously explained

    def apply_effect(self, ball, paddle):  # previously explained
        spell_sound = pygame.mixer.Sound("sounds/spell.wav")  # previously explained
        spell_sound.set_volume(0.3)  # previously explained
        if self.rect.colliderect(paddle.rect):  # previously explained
            spell_sound.play()  # previously explained
            if ball.speed_x > 0 and ball.speed_y > 0:  # previously explained
                ball.speed_x -= boost_speed_decrease
                ball.speed_y -= boost_speed_decrease
            elif ball.speed_x < 0 < ball.speed_y:
                ball.speed_x += boost_speed_decrease
                ball.speed_y -= boost_speed_decrease
            elif ball.speed_x > 0 > ball.speed_y:
                ball.speed_x -= boost_speed_decrease
                ball.speed_y += boost_speed_decrease
            elif ball.speed_x < 0 and ball.speed_y < 0:
                ball.speed_x += boost_speed_decrease
                ball.speed_y += boost_speed_decrease
            self.rect.y = window_height  # previously explained
            del self  # previously explained
        elif self.rect.top >= window_height:  # previously explained
            del self  # previously explained

    def check_collision(self, obj):  # previously explained
        return self.rect.colliderect(obj)  # previously explained
