import sys
sys.path.append('/Users/Hackintosh/Dropbox/Python/Projects/Chip8/Chip8')
import numpy as np
from Opcode_interpreter import interpretOpcode

MAX_MEMORY = 4096

class Chip8:

    def __init__(self):
        opcode = np.uint16

        self.memory = np.zeros([4096], dtype=np.uint8)
        self.pc = 0x200
        self.reg_V = np.zeros(16, dtype=np.uint8)

        self.I = np.uint16(0x0)

        self.stack = [0]*16
        self.stack_pointer = 0

        self.delay_timer = 0
        self.sound_timer = 0

        self.keys = np.zeros(16, dtype=np.uint8)

        self.display = np.zeros((64 * 32), dtype=np.uint8)


    def run(self):
        # fetch opcode
        opcode = (self.memory[self.pc] << 8) | self.memory[self.pc + 1]
        print(hex(opcode), ': ')
        interpretOpcode(opcode)
        # decode opcode



            #execute opcode





def Main():
    chip8 = Chip8()
    # z = 0
    # for i in range(len(chip8.memory)):
    #     chip8.memory[z] = 0xFF
    #     print(hex(chip8.memory[z]))
    #     z += 1

    chip8.run()

    #for x in chip8.stack:
    #    print(x)

if __name__ == "__main__":
    Main()