import pygame
from pygame.locals import *
import time
import random

# Global variables
SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120

    def draw(self):
        # draw the apple
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        # move the apple randomly
        # values set as multiples of 1000 and 800 for x/y
        self.x = random.randint(1, 24) * SIZE
        self.y = random.randint(1, 19) * SIZE


class Snake:
    def __init__(self, parent_screen):
        # storing class members
        self.parent_screen = parent_screen
        self.length = 1

        # create the first block
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x = [40]
        self.y = [40]

        # default direction
        self.direction = 'down'

    # increase the snake's length when eating an apple
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):

        for i in range(self.length):
            # draw the block dynamically
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))

        # updating the screen
        pygame.display.flip()

    # creating movement functions
    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    # perpetuating the snakes movement
    def slither(self):

        # iterate backwards for every previous block
        for i in range(self.length - 1, 0, -1):
            # update snake's body
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # update snake's head
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE

        self.draw()


class Game:
    def __init__(self):
        # initializing the game
        pygame.init()
        pygame.display.set_caption("Snake")
        pygame.mixer.init()

        # play the background music!
        self.play_background_music()

        # creating a surface
        self.surface = pygame.display.set_mode((1000, 800))

        # rendering the background color
        self.render_background()

        # creating the snake and apple objects
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

        # draw the snake/apple
        self.snake.draw()
        self.apple.draw()

    def collision(self, x1, y1, x2, y2):
        # if the snake's head position
        if x2 <= x1 < x2 + SIZE:
            #  falls anywhere within the apples position
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    def play_sound(self, sound):
        sounds = pygame.mixer.Sound(f"resources/{sound}.mp3")
        pygame.mixer.Sound.play(sounds)

    def play_background_music(self):
        pygame.mixer.music.load('resources/bg_music_1.mp3')
        pygame.mixer.music.play()

    def render_background(self):
        bg = pygame.image.load('resources/background.jpg')
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.snake.slither()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        # if the snake's head intersects with an apple
        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            # create an apple bite sound!
            self.play_sound("Apple-bite")

            # increase the snakes length by 1
            self.snake.increase_length()

            # and move the apple to a random position
            self.apple.move()

        # if the snake collides with itself
        for i in range(3, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                # create a crash sound!
                self.play_sound("crash")
                raise Exception("Game over")

    def game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        game_over_message = font.render(f'Game Over! Your score is: {self.snake.length}', True, (255, 255, 255))
        self.surface.blit(game_over_message, (200, 300))
        play_again = font.render('Press Enter to play again or press Escape to exit', True, (255, 255, 255))
        self.surface.blit(play_again, (200, 350))

        pygame.display.flip()
        pygame.mixer.music.pause()

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f'Score: {self.snake.length}', True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def display_paused(self):
        font = pygame.font.SysFont('arial', 40)
        paused = font.render('PAUSED', True, (255, 255, 255))
        self.surface.blit(paused, (400, 400))
        pygame.display.flip()
        pygame.mixer.music.pause()

    def reset(self):
        # creating the snake and apple objects
        self.snake = Snake(self.surface)
        self.apple = Apple(self.surface)

    def run(self):
        # event loop for starting/ending the game
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    # pause the game
                    if event.key == K_RETURN:
                        if not pause:
                            pause = True
                            self.display_paused()
                        else:
                            pygame.mixer.music.unpause()
                            pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()

                        if event.key == K_DOWN:
                            self.snake.move_down()

                        if event.key == K_LEFT:
                            self.snake.move_left()

                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            # play if the game is not paused
            try:
                if not pause:
                    self.play()

            # pause the game is over
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()

            # time between snake movements
            time.sleep(0.25)


# initializing the module
if __name__ == "__main__":
    # running the game
    game = Game()
    game.run()
