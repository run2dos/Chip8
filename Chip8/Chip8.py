import sys, os
home = os.getenv("HOME")
home += "/Dropbox/Python/Projects/Chip8/Chip8/"
sys.path.append(home)

import numpy as np

MAX_MEMORY = 4096

class Chip8:

    display = np.zeros((64 * 32), dtype=np.uint8)

    def __init__(self):
        opcode = np.uint16

        self.memory = np.zeros([4096], dtype=np.uint8)
        self.romSize = np.zeros([0], dtype=np.uint8)

        self.pc = 0x200
        self.reg_V = np.zeros(16, dtype=np.uint8)

        self.I = np.uint16(0x0)

        self.stack = [0]*16
        self.stack_pointer = 0

        self.delay_timer = 0
        self.sound_timer = 0

        self.keys = np.zeros(16, dtype=np.uint8)

        self.needsReDraw = False

    @classmethod
    def get_display(cls):
        """Returns Current Value of the display"""
        return Chip8.display

    @classmethod
    def display_test(cls, x, state):
        """Method that makes it easier to test the display"""
        Chip8.display[x]=state
        Chip8.display[x + (64 * 8)]=state
        Chip8.display[x + (64 * 16)]=state
        Chip8.display[x + (64 * 24)]=state


    def run(self):
        """Fetches, Decodes, and Executes Opcode"""
        # fetch opcode
        opcode = (self.memory[self.pc] << 8) | self.memory[self.pc + 1]
        # print(hex(opcode), ': ', end='')
        interpreter.interpretOpcode(opcode)
        # decode opcode

            #execute opcode


    def incrementPC(self, inc):
        """Increments the Program Counter by the inc amount"""
        self.pc += inc


    def needsReDrawn(self):
        """Returns the current bool value of the needsReDraw flag"""
        return self.needsReDraw

    def removeDrawFlag(self):
        """Turns the needsReDraw flag false"""
        self.needsReDraw = False


    def loadRom(self, romLocation):
        """Loads rom into Memory"""
        f = open(romLocation, 'r')
        rom = f.read()
        f.close()
        rom = rom.replace('\n', ' ')
        self.romSize = len(rom.split())
        temp = ''

        for idx, x in enumerate(range(0x200,(0x200 + self.romSize))):
            self.memory[x] = int(rom.split()[idx], 16)







class interpreter:

    def Opcode0(opcode):
        print(hex(opcode), end=': ')
        NNN = 0xFFF & opcode
        if (opcode & 0x00FF) == 0x00EE:
            print('00EE Return from a subroutine.')

        elif (opcode & 0x00F0) == 0x00E0:
            print('00E0 Clear Screen')

        else:
            print('0NNN Execute machine langage subroutine at address NNN', 'Addr_NNN='+hex(NNN))



    def Opcode1(opcode):
        print(hex(opcode), end= ': ')
        NNN = 0xFFF & opcode
        print('1NNN Jump to address NNN', 'Addr_NNN='+hex(NNN))



    def Opcode2(opcode):
        print(hex(opcode), end= ': ')
        NNN = 0xFFF & opcode
        print('2NNN Execute subroutine starting at address NNN', 'Addr_NNN='+hex(NNN))


      
    def Opcode3(opcode):
        print(hex(opcode), end= ': ')
        VX, NN = (opcode & 0x0F00) >> 8, opcode & 0x00FF
        print('3XNN Skip the following instruction if the value of register VX equals NN', 'reg_VX='+hex(VX), 'value_NN='+hex(NN))


      
    def Opcode4(opcode):
        print(hex(opcode), end= ': ')
        VX, NN = (opcode & 0x0F00) >> 8, opcode & 0x00FF
        print('4XNN Skip the following instruction if the value of register VX is not equal to NN', 'reg_VX='+hex(VX), 'value_NN='+hex(NN))


      
    def Opcode5(opcode):
        print(hex(opcode), end= ': ')
        VX, VY = (opcode & 0x0F00) >> 8, (opcode & 0x00F0) >> 4
        if (opcode & 0x000F) == 0x0000:
            print('5XY0 Skip the following instruction if the value of register VX is equal to the value of register VY', 'reg_VX='+hex(VX), 'regVY='+hex(VY))
        else:
            print('This opcode does not exist!')

      
    def Opcode6(opcode):
        print(hex(opcode), end= ': ')
        VX, NN = (opcode & 0x0F00) >> 8, opcode & 0x00FF
        print('6XNN Store number NN in register VX', 'reg_VX='+hex(VX), 'value_NN='+hex(NN))


      
    def Opcode7(opcode):
        print(hex(opcode), end= ': ')
        VX, NN = (opcode & 0x0F00) >> 8, opcode & 0x00FF
        print('7XNN Add the value NN to register VX', 'reg_VX='+hex(VX), 'value_NN='+hex(NN))


      
    def Opcode8(opcode):
        print(hex(opcode), end= ': ')
        VX, VY = (opcode & 0x0F00) >> 8, (opcode & 0x00F0) >> 4
        if (opcode & 0x000F) == 0x0000:
            print('8XY0 Store the value of register VY in register VX', 'reg_VX='+hex(VX), 'regVY='+hex(VY))

        elif (opcode & 0x000F) == 0x0001:
            print('8XY1 Set VX to VX OR VY', 'reg_VX='+hex(VX), 'regVY='+hex(VY))

        elif (opcode & 0x000F) == 0x0002:
            print('8XY2 Set VX to VX AND VY', 'reg_VX='+hex(VX), 'regVY='+hex(VY))

        elif (opcode & 0x000F) == 0x0003:
            print('8XY3 Set VX to VX XOR VY', 'reg_VX='+hex(VX), 'regVY='+hex(VY))

        elif (opcode & 0x000F) == 0x0004:
            print('8XY4 Add the value of register VY to register VX Set VF to 01 if a carry occurs Set VF to 00 if a carry does not occur', 'reg_VX='+hex(VX), 'regVY='+hex(VY))

        elif (opcode & 0x000F) == 0x0005:
            print('8XY5 Subtract the value of register VY from register VX Set VF to 00 if a borrow occurs Set VF to 01 if a borrow does not occur', 'reg_VX='+hex(VX), 'regVY='+hex(VY))

        elif (opcode & 0x000F) == 0x0006:
            print('8XY6 Store the value of register VY shifted right one bit in register VX Set register VF to the least significant bit prior to the shift', 'reg_VX='+hex(VX), 'regVY='+hex(VY))

        elif (opcode & 0x000F) == 0x0007:
            print('8XY7 Set register VX to the value of VY minus VX Set VF to 00 if a borrow occurs Set VF to 01 if a borrow does not occur', 'reg_VX='+hex(VX), 'regVY='+hex(VY))

        elif (opcode & 0x000F) == 0x000E:
            print('8XYE Store the value of register VY shifted left one bit in register VX Set register VF to the most significant bit prior to the shift', 'reg_VX='+hex(VX), 'regVY='+hex(VY))
      
        else:
            print('This opcode does not exist!')
      


    def Opcode9(opcode):
        print(hex(opcode), end= ': ')
        VX, VY = (opcode & 0x0F00) >> 8, (opcode & 0x00F0) >> 4
        if (opcode & 0x000F) == 0x0000:
            print('9XY0 Skip the following instruction if the value of register VX is not equal to the value of register VY', 'reg_VX='+hex(VX), 'regVY='+hex(VY))
        else:
            print('This opcode does not exist!')


    def OpcodeA(opcode):
        print(hex(opcode), end= ': ')
        NNN = 0xFFF & opcode
        print('ANNN Store memory address NNN in register I', 'Addr_NNN='+hex(NNN))
      


    def OpcodeB(opcode):
        print(hex(opcode), end= ': ')
        NNN = 0xFFF & opcode
        print('BNNN Jump to address NNN + V0', 'Addr_NNN='+hex(NNN))
      


    def OpcodeC(opcode):
        print(hex(opcode), end= ': ')
        VX, NN = (opcode & 0x0F00) >> 8, opcode & 0x00FF
        print('CXNN Set VX to a random number with a mask of NN', 'reg_VX='+hex(VX), 'value_NN='+hex(NN))
      


    def OpcodeD(opcode):
        print(hex(opcode), end= ': ')
        VX, VY, N = (opcode & 0x0F00) >> 8, (opcode & 0x00F0) >> 4, opcode & 0x000F
        print('DXYN Draw a sprite at position VX, VY with N bytes of sprite data starting at the address stored in I Set VF to 01 if any set pixels are changed to unset, and 00 otherwise', 'reg_VX='+hex(VX), 'reg_VY='+hex(VY), 'N='+hex(N))
      


    def OpcodeE(opcode):
      print(hex(opcode), end= ': ')
      VX = (opcode & 0x0F00) >> 8
      if (int(opcode) & 0xF0FF) == 0xE09E:
          print('EX9E Skip the following instruction if the key corresponding to the hex value currently stored in register VX is pressed', 'reg_VX='+hex(VX))

      elif (opcode & 0xF0FF) == 0xE0A1:
          print('EXA1 Skip the following instruction if the key corresponding to the hex value currently stored in register VX is not pressed', 'reg_VX='+hex(VX))

      else:
          print('This opcode does not exist!')
      


    def OpcodeF(opcode):
        print(hex(opcode), end= ': ')
        VX = (opcode & 0x0F00) >> 8 
        if (opcode & 0x00FF) == 0x0007:
            print('FX07 Sets VX to the value of the delay timer.', 'reg_VX='+hex(VX))

        elif (opcode & 0x00FF) == 0x000A:
            print('FX0A A key press is awaited, and then stored in VX.', 'reg_VX='+hex(VX))

        elif (opcode & 0x00FF) == 0x0015:
            print('FX15 Sets the delay timer to VX.', 'reg_VX='+hex(VX))

        elif (opcode & 0x00FF) == 0x0018:
            print('FX18 Sets the sound timer to VX.', 'reg_VX='+hex(VX))

        elif (opcode & 0x00FF) == 0x001E:
            print('FX1E Adds VX to I.', 'reg_VX='+hex(VX))

        elif (opcode & 0x00FF) == 0x0029:
            print('FX29 Sets I to the location of the sprite for the character in VX. Characters 0-F (in hexadecimal) are represented by a 4x5 font.', 'reg_VX='+hex(VX))

        elif (opcode & 0x00FF) == 0x0033:
            print('FX33 Stores the Binary-coded decimal representation of VX, with the most significant of three digits at the address in I, the middle digit at I plus 1, and the least significant digit at I plus 2. (In other words, take the decimal representation of VX, place the hundreds digit in memory at location in I, the tens digit at location I+1, and the ones digit at location I+2.)', 'reg_VX='+hex(VX))

        elif (opcode & 0x00FF) == 0x0055:
            print('FX55 Stores V0 to VX in memory starting at address I.', 'reg_VX='+hex(VX))

        elif (opcode & 0x00FF) == 0x0065:
            print('FX65 Fills V0 to VX with values from memory starting at address I.', 'reg_VX='+hex(VX))

        else:
            print('This opcode does not exist!')



    OpcodePrefix = {0x0000: Opcode0,
             0x1000: Opcode1,
             0x2000: Opcode2,
             0x3000: Opcode3,
             0x4000: Opcode4,
             0x5000: Opcode5,
             0x6000: Opcode6,
             0x7000: Opcode7,
             0x8000: Opcode8,
             0x9000: Opcode9,
             0xA000: OpcodeA,
             0xB000: OpcodeB,
             0xC000: OpcodeC,
             0xD000: OpcodeD,
             0xE000: OpcodeE,
             0xF000: OpcodeF
    }

    def interpretOpcode(opcode):
      if (opcode & 0xF000) not in interpreter.OpcodePrefix:
          OpcodeDoesNotExist()
      else:
          interpreter.OpcodePrefix[opcode & 0xF000](opcode)
          # OpcodePrefix[opcode & 0xF000](str(opcode))




def Main():
    chip8 = Chip8()
    # z = 0
    # for i in range(len(chip8.memory)):
    #     chip8.memory[z] = 0xFF
    #     print(hex(chip8.memory[z]))
    #     z += 1
    # for x in chip8.get_display():
    #     print(x)
    chip8.loadRom('/Volumes/Macintosh HD/Users/HGHRLLR/Python/projects/Chip8/rom/Fishie.ch8')
    for x in range(chip8.romSize):
        chip8.run()
        chip8.incrementPC(2)
    #for x in chip8.stack:
    #    print(x)

if __name__ == "__main__":
    Main()