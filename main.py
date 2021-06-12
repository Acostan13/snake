import pygame
from pygame.locals import *


def draw_block():
    # giving the surface color
    surface.fill((3, 144, 252))

    # draw the block
    surface.blit(block, (block_x, block_y))

    # updating the screen
    pygame.display.flip()


# initializing the module
if __name__ == "__main__":
    pygame.init()

    # creating a surface
    surface = pygame.display.set_mode((1000, 500))

    # create the first block
    block = pygame.image.load("resources/block.jpg").convert()
    block_x = 100
    block_y = 100
    surface.blit(block, (block_x, block_y))

    # updating the screen
    pygame.display.flip()

    # event loop for starting/ending the game
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()

            elif event.type == QUIT:
                running = False
