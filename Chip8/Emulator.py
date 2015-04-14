import sys, os
home = os.getenv("HOME")
home += "/Dropbox/Python/Projects/Chip8/Chip8/"
sys.path.append(home)

import numpy as np
from Chip8 import Chip8
from Display import TextDisplay

from time import sleep



def Main():

    chip = Chip8()
    test = TextDisplay(chip)
    for x in range(64 * 8):
        chip.display_test(x, 1)
        test.paint()        
        sleep(.024)
    #chip.run()


if __name__ == '__main__':
    Main()