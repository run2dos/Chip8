import sys, os, math, pygame, time
from Chip8 import Chip8


BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

display_width = 640
display_height = 320
frames_per_second = 30

class Display:
    def __init__(self, Chip):
        self.chip = Chip
        self.display = self.chip.display
        self.title = 'CHIMP ATE'
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.gameDisplay.fill(BLACK)

    def draw_pixel(self, x, y, width, height, color):
        pygame.draw.rect(self.gameDisplay, color, [x, y, width, height])


    def draw(self):
        #self.display[63]=1
        #print(self.display)
        for idx, pixel in enumerate(self.display):
            if pixel == 0:
                color = WHITE
            else:
                color = BLACK

            x = (idx % 64)
            y = math.floor(idx / 64)

            self.draw_pixel(x * 10, y * 10, 10, 10, color)


    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            print(event)
           
        self.draw()

        pygame.display.update()
        self.clock.tick(frames_per_second)

def Main():
    chip = Chip8()
    display = Display(chip)
    display.run()
    pygame.quit()
    quit()

if __name__ == '__main__':
    Main()
