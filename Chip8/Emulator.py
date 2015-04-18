import sys, os, threading
home = os.getenv("HOME")
home += "/Dropbox/Python/Projects/Chip8/Chip8/"
gamelocation = os.getenv("HOME")
gamelocation += '/Dropbox/Python/Projects/Chip8/bin'

sys.path.append(home)

import numpy as np
from Chip8 import Chip8
from Display import TextDisplay
from Display3 import Display
from Chip8_Debugger import Debugger

from time import sleep

class Main(threading.Thread):
    def __init__(self):
        romName = 'MAZE'
        self.chip = Chip8()
        self.display = TextDisplay(self.chip)
        self.chip.loadRom('../rom/' + romName)
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while(True):
            self.chip.run()
            if self.chip.needsReDrawn():
                self.display.paint()
                self.chip.removeDrawFlag()
            sleep(0.016)

class Main2(threading.Thread):
    def __init__(self):
        romName = 'MAZE'
        self.chip = Chip8()
        self.display = Display(self.chip)
        self.chip.loadRom('../rom/' + romName)
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while(True):
            self.chip.run()
            if self.chip.needsReDrawn():
                self.display.run()
                self.chip.removeDrawFlag()
            sleep(0.016)

if __name__ == '__main__':
    print('pree main')

    main = Main2()
    # debug = Debugger(main.chip).run()
