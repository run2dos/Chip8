import pygame
import time



BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

display_width = 800
display_height = 600
frames_per_second = 30


pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CHIP EIGHT')
clock = pygame.time.Clock()


def box(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])



def game_loop():

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # print(event)


        gameDisplay.fill(WHITE)



        box(0,0,10,10,BLACK)

        pygame.display.update()
        clock.tick(frames_per_second)



game_loop()
pygame.quit()
quit()