import sys, os

home = os.getenv("HOME")
home += "/Dropbox/Python/Projects/Chip8/Chip8/"
sys.path.append(home)

import numpy as np
import math

from Chip8 import Chip8


class TextDisplay:
    def __init__(self, Chip8):
        self.chip = Chip8
        self.display = self.chip.get_display()
        self.title = '               Welcome to the Chip 8 interpreter.'

    def paint(self):
        print(self.title)
        for idx,pixel in enumerate(self.display):

            x = (idx % 64)
            y = math.floor(idx / 64)
            
            if x % 64 == 0:
                print()
            else:
                if pixel == 0:
                    print('.', end='')
                else:
                    print('#', end='')
        print('\n')

    def test(self):
        from time import sleep
        for x in range(64 * 8):
            self.chip.display_test(x, 1)
            sleep(.25)
            self.paint()

def main():
    TextDisplay(Chip8()).test()

if __name__ == '__main__':
    main()