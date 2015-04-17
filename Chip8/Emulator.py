import sys, os, threading
home = os.getenv("HOME")
home += "/Dropbox/Python/Projects/Chip8/Chip8/"
gamelocation = os.getenv("HOME")
gamelocation += '/Dropbox/Python/Projects/Chip8/bin'

sys.path.append(home)

import numpy as np
from Chip8 import Chip8
from Display import TextDisplay

from time import sleep

class Main(threading.Thread):

    chip = Chip8()
    display = TextDisplay(chip)
    chip.loadRom('/Volumes/Macintosh HD/Users/HGHRLLR/Python/projects/Chip8/rom/Fishie.ch8')

    def run(self):
        while(True):
            Main.chip.run()
            if Main.chip.needsReDrawn():
                Main.display.paint()
                Main.chip.removeDrawFlag()
            sleep(0.016)


if __name__ == '__main__':
    main = Main()
    main.start()