import pygame
from pygame.locals import *
import time

# Global variables
SIZE = 40


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        # draw the apple
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

class Snake:
    def __init__(self, parent_screen, length):
        # storing class members
        self.parent_screen = parent_screen
        self.length = length

        # create the first block
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x, self.y = [SIZE] * length, [SIZE] * length

        # default direction
        self.direction = 'down'

    def draw(self):
        # giving the surface color
        self.parent_screen.fill((3, 144, 252))

        for i in range(self.length):
            # draw the block
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
    def walk(self):

        # iterate backwards for every previous block
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

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

        # creating a surface
        self.surface = pygame.display.set_mode((1000, 800))

        # giving the surface color
        self.surface.fill((3, 144, 252))

        # creating the snake and apple objects
        self.snake = Snake(self.surface, 6)
        self.apple = Apple(self.surface)

        # draw the snake/apple
        self.snake.draw()
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        # event loop for starting/ending the game
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

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

            # play the game!
            self.play()

            time.sleep(0.3)


# initializing the module
if __name__ == "__main__":

    # running the game
    game = Game()
    game.run()


