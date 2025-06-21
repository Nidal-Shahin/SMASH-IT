# SMASH IT! 💥
A fast-paced arcade game developed using Pygame.

## About the Game
"SMASH IT!" is a classic arcade-style brick-breaker game developed using the Pygame library in Python. The objective is simple: control a paddle at the bottom of the screen to bounce a ball 🏐, destroy all the bricks at the top, and achieve the highest score possible. Be careful not to let the ball fall off the screen, as you have a limited number of lives ❤️!

## Features
- **Dynamic Gameplay:** Engage in a fast-paced brick-breaking experience with a responsive ball and paddle. 🎾

- **Multi-Layered Bricks:** Encounter four different types of bricks (Emerald 💎, Gold 💰, Stone 🗿, Wood 🪵), each requiring a specific number of hits to destroy, adding strategic depth.

- **Power-Up System:** Collect randomly generated boosts ✨ that fall from destroyed bricks, including:

    - Paddle Width Increase/Decrease ↔️

    - Ball Speed Increase/Decrease ⚡

    - Life Increase/Decrease ❤️‍🩹

- **Life System:** Start with a set number of lives, visually represented by hearts, and manage them carefully to avoid a game over. 💖

- **Scoring:** Track your progress with an on-screen score that updates as you destroy bricks. 🏆

- **Immersive Sound Design:** Enjoy a full audio experience with background music 🎵, sound effects for ball-paddle collisions, ball-brick hits (unique for each brick type), and boost collection. 🔊

- **Intuitive Controls:** Simple and easy-to-learn controls allow for immediate pickup and play. 🎮

- **Start and End Screens:** Features a welcoming start screen 👋 and distinct winning/losing screens to enhance the player experience. 🎉😔

## Installation
To run "SMASH IT!" on your local machine, follow these steps:

**Prerequisites**
- Python 3.x

- Pygame library

You can install Pygame using pip:
```
pip install pygame
```
**Running the Game**
- **Download the files:**
    - Download all the game files (Python scripts, images folder, sounds folder) into a single directory. 📂

- **Navigate to the game directory:**
    - Open your terminal or command prompt, navigate to the directory where you saved the game files:
    ```
    cd path/to/your/SMASH-IT-folder
    ```
- **Run the main game file:**
    ```
    python main.py
    ```
## How to Play
The game starts with an introductory image. Press the SPACEBAR to begin. Control the paddle to prevent the ball from falling off the bottom of the screen. Your goal is to bounce the ball into the bricks above, destroying them layer by layer. Each brick type requires a different number of hits to be removed. Random boosts will appear after certain scores are reached; catch them with your paddle to activate their effects. Destroy all 32 bricks to win the game. If you lose all your lives, it's game over! 🕹️

## Controls
- **SPACEBAR:** Start the game (from the title screen). ▶️

- **LEFT Arrow Key:** Move the paddle left. ◀️

- **RIGHT Arrow Key:** Move the paddle right. ▶️

## File Structure
```
SMASH-IT/
├── main.py             # Main game loop, initialization, and game flow control.
├── ball.py             # Defines the Ball class, handling its movement, collisions, and resets.
├── paddle.py           # Defines the Paddle class, managing its movement and interaction with screen boundaries.
├── bricks.py           # Defines the Brick class and various Layer classes, managing brick types, hits, and rendering.
├── boosts.py           # Defines the base Boosts class and its subclasses for different power-ups (e.g., paddle size, ball speed, lives).
├── heart.py            # Defines the Heart class and Hearts manager, displaying and managing player lives.
├── settings.py         # Stores global game variables, such as window dimensions, speeds, and object sizes, and functions for modifying them.
├── images/             # Contains all image assets (ball, paddle, bricks, backgrounds, boost icons, etc.).
│   ├── ball.png
│   ├── bg.jpg
│   ├── emerald-bricks.png
│   ├── goldBrick.png
│   ├── heart.png
│   ├── heartDecrease.png
│   ├── heartIncrease.png
│   ├── icon.jpg
│   ├── you-lost.jpg
│   ├── paddle.png
│   ├── sizeDecrease.png
│   ├── sizeIncrease.png
│   ├── speedDecrease.png
│   ├── speedIncrease.png
│   ├── start-image.jpg
│   ├── stoneBrick.png
│   ├── winning_image2.jpg
│   └── woodBrick.png
└── sounds/             # Contains all sound effects and background music for the game.
    ├── BoostCollect.wav
    ├── blood-pop.wav
    ├── game-music.mp3
    ├── gem-hit.wav
    ├── gold-hit.wav
    ├── losing-sound.wav
    ├── paddle-hit.wav
    ├── sides-hit.wav
    ├── spell.wav
    ├── stone-hit.wav
    ├── winning-sound.wav
    └── wood-hit.wav
```
## Credits
- **Game Development:** Nidal Shahin (me) 🧑‍💻

- **University:** Jordan University of Science and Technology 🎓

- **Course:** Artificial Intelligence Programming (Python) 📚

- **Special Thanks:** Dr. Malak Abdullah, the supervisor and teacher of this course 🙏

## License
This is a university project created for educational purposes. All rights reserved. ©
