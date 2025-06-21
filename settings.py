# Game window dimensions
window_width = 880  # static
window_height = 660  # static

# ---------------------------------------
# Paddle settings
paddle_width = 120
paddle_height = 50
paddle_speed = 7


def default_size():  # restores the default size of the paddle
    global paddle_height, paddle_width
    paddle_width = 120
    paddle_height = 50


def increment_size():  # increments the dimensions by fixed values
    global paddle_height, paddle_width
    paddle_height += 10
    paddle_width += 40


def decrement_size():  # decrements the dimensions by fixed values
    global paddle_height, paddle_width
    paddle_height -= 10
    paddle_width -= 40


def return_width():  # returns the paddle width
    return paddle_width


def return_height():  # returns the paddle height
    return paddle_height


# ---------------------------------------
# Ball settings
ball_speed_x = 5
ball_speed_y = -5


def default_speed_x():  # restores the default value of the balls x-speed
    global ball_speed_x
    ball_speed_x = 5
    return ball_speed_x


def default_speed_y():  # restores the default value of the balls y-speed
    global ball_speed_y
    ball_speed_y = -5
    return ball_speed_y


# ---------------------------------------
# Brick settings
brick_width = 109.00075  # width,height,x and y spacing are calculated to fit the screen and to achieve the desired shape
brick_height = 44.040707072
brick_spacing_x = 1.142
brick_spacing_y = 10
brick_cols = 8  # meant to be static
brick_rows = 4  # meant to be static

# ---------------------------------------
# Set up game variables
score = 0  # gets incremented whenever a brick is destroyed
lives = 3  # gets decremented by the ball falling off the screen and by the life decreasing boost


def increment_lives():  # increments lives
    global lives
    lives += 1


def decrement_lives():  # decrements lives
    global lives
    lives -= 1


def get_lives():  # returns lives value
    return lives


# ---------------------------------------
# Boosts
boost_speed_x = 0  # speed of the falling boost object
boost_speed_y = 1  # speed of the falling boost object
boost_width = 50  # width of the boost image
boost_height = 50  # height of the boost image
boost_speed_decrease = 2  # ball speed boost
boost_speed_increase = 2  # ball speed boost
