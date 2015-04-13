import numpy as np

MAX_MEMORY = 4096

class Chip8:

    def __init__(self):
        opcode = np.uint16

        self.memory = np.zeros([4096], dtype=np.uint8)
        self.reg_V = np.zeros(16, dtype=np.uint8)

        self.I = np.uint16(0x0)

        self.stack = [0]*16
        self.stack_pointer = 0

        self.delay_timer = 0
        self.sound_timer = 0

        self.keys = np.zeros(16, dtype=np.uint8)







chip8 = Chip8()

for x in chip8.stack:
    print(x)