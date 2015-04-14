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

    def paint(self):
        for idx,pixel in enumerate(self.display):

            x = (idx % 64)
            y = math.floor(idx / 64)
            
            if x % 64 == 0:
                print()
            else:
                if pixel == 0:
                    print(' ', end='')
                else:
                    print('#', end='')
