import pygame
from pygame.locals import *
import time


class Snake:
    def __init__(self, surface):
        # storing the screen as a class member
        self.parent_screen = surface

        # create the first block
        self.block = pygame.image.load("resources/block.jpg").convert()
        self.x, self.y = 100, 100

        # default direction
        self.direction = 'down'

    def draw(self):
        # giving the surface color
        self.parent_screen.fill((3, 144, 252))

        # draw the block
        self.parent_screen.blit(self.block, (self.x, self.y))

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
        if self.direction == 'up':
            self.y -= 10
        if self.direction == 'down':
            self.y += 10
        if self.direction == 'left':
            self.x -= 10
        if self.direction == 'right':
            self.x += 10

        self.draw()


class Game:
    def __init__(self):
        # initializing the game
        pygame.init()

        # creating a surface
        self.surface = pygame.display.set_mode((500, 500))

        # giving the surface color
        self.surface.fill((3, 144, 252))

        # creating the snake
        self.snake = Snake(self.surface)

        # draw the snake
        self.snake.draw()

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

            self.snake.walk()
            time.sleep(0.2)


# initializing the module
if __name__ == "__main__":

    # running the game
    game = Game()
    game.run()


