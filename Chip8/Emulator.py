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
    #chip.loadProgram('Fishie.ch8')

    def run(self):
        #run_thread = threading.Thread(target=cls.chip.run).start()
        while(True):
            Main.chip.run()
            if Main.chip.needsReDrawn():
                Main.display.paint()
                Main.chip.removeDrawFlag()
            sleep(0.016)



    #@classmethod
    #def test_run(cls):
    #    for x in range(64 * 8):
    #        cls.chip.display_test(x, 1)
    #        cls.display.paint()        
    #        sleep(.024)
    #        cls.chip.run()


if __name__ == '__main__':
    main = Main()
    main.start()