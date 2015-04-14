import sys, os
home = os.getenv("HOME")
home += "/Dropbox/Python/Projects/Chip8/Chip8/"
sys.path.append(home)

import numpy as np
from Chip8 import Chip8
from Display import TextDisplay



def Main():

    chip = Chip8()
    test = TextDisplay(chip)
    test.paint()
    chip.run()


if __name__ == '__main__':
    Main()