class interpreter:

  def Opcode0(x):
      print(hex(x), end=': ')

      if (x & 0x00F0) == 0x00E0:
          print('00E0 Clear Screen')

      elif (x & 0x00FF) == 0x00EE:
          print('00EE Return from a subroutine.')

      else:
          print('0NNN Execute machine langage subroutine at address NNN', 'Addr_NNN='+interpreter.GetOpcodeAddressNNN(x))

  def Opcode1(x):
      print('1NNN Jump to address NNN', 'Addr_NNN='+GetOpcodeAddressNNN(x))
      
  def Opcode2(x):
      print('2NNN Execute subroutine starting at address NNN', 'Addr_NNN='+GetOpcodeAddressNNN(x))
      
  def Opcode3(x):
      print(hex(x), end= ' ')
      VX, NN = x & 0x0F00, x & 0x00FF
      print('3XNN Skip the following instruction if the value of register VX equals NN', 'reg_VX='+hex(VX), 'value_NN='+hex(NN))
      
  def Opcode4(x):
      print('4XNN Skip the following instruction if the value of register VX is not equal to NN', 'reg_VX='+x[1], 'value_NN='+x[2:])
      
  def Opcode5(x):
      print('5XY0 Skip the following instruction if the value of register VX is equal to the value of register VY', 'reg_VX='+x[1], 'regVY='+x[2])
      
  def Opcode6(x):
      print('6XNN Store number NN in register VX', 'reg_VX='+x[1], 'value_NN='+x[2:])
      
  def Opcode7(x):
      print('7XNN Add the value NN to register VX', 'reg_VX='+x[1], 'value_NN='+x[2:])
      
  def Opcode8(x):
    if (int(x) & 0x000F) == 0x0000:
      print(hex(int(x)), '8000')

    elif (int(x) & 0x000F) == 0x0001:
      print(hex(int(x)), '8001')

    elif (int(x) & 0x000F) == 0x0002:
      print(hex(int(x)), '8002')

    elif (int(x) & 0x000F) == 0x0003:
      print(hex(int(x)), '8003')

    elif (int(x) & 0x000F) == 0x0004:
      print(hex(int(x)), '8004')

    elif (int(x) & 0x000F) == 0x0005:
      print(hex(int(x)), '8005')

    elif (int(x) & 0x000F) == 0x0006:
      print(hex(int(x)), '8006')

    elif (int(x) & 0x000F) == 0x0007:
      print(hex(int(x)), '8007')
    elif (int(x) & 0x000F) == 0x000E:
      print(hex(int(x)), '800E')
    else:
      print(hex(int(x)), 'Not Handled yet!')
      
  def Opcode9(x):
      print('9XY0 Skip the following instruction if the value of register VX is not equal to the value of register VY', 'reg_VX='+x[1], 'regVY='+x[2])
      
  def OpcodeA(x):
      print('ANNN Store memory address NNN in register I', 'Addr_NNN='+x[1:4])
      
  def OpcodeB(x):
      print('BNNN Jump to address NNN + V0', 'Addr_NNN='+x[1:4])
      
  def OpcodeC(x):
      print('CXNN Set VX to a random number with a mask of NN', 'reg_VX='+x[1], 'value_NN='+x[2:])
      
  def OpcodeD(x):
      print("""DXYN Draw a sprite at position VX, VY with N bytes of sprite data starting at the address stored in I Set VF to 01 if any set pixels are changed to unset, and 00 otherwise""")
      
  def OpcodeE(x):

    if (int(x, 16) & 0xF0FF) == 0xE09E:
      print(x, 'EX9E Skip the following instruction if the key corresponding to the hex value currently stored in register VX is pressed')
    elif (int(x, 16) & 0xF0FF) == 0xE0A1:
      print(x, 'EXA1 Skip the following instruction if the key corresponding to the hex value currently stored in register VX is not pressed')
    else:
      print(x, 'Does not exist.')
      
  def OpcodeF(x):
    x = int(x, 16)
    if (x & 0x00FF) == 0x0007:
      print(hex(x), 'FX07 Sets VX to the value of the delay timer.')
    elif (x & 0x00FF) == 0x000A:
      print(hex(x), 'FX0A A key press is awaited, and then stored in VX.')
    elif (x & 0x00FF) == 0x0015:
      print(hex(x), 'FX15 Sets the delay timer to VX.')
    elif (x & 0x00FF) == 0x0018:
      print(hex(x), 'FX18 Sets the sound timer to VX.')
    elif (x & 0x00FF) == 0x001E:
      print(hex(x), 'FX1E Adds VX to I.')
    elif (x & 0x00FF) == 0x0029:
      print(hex(x), 'FX29 Sets I to the location of the sprite for the character in VX. Characters 0-F (in hexadecimal) are represented by a 4x5 font.')
    elif (x & 0x00FF) == 0x0033:
      print(hex(x), 'FX33 Stores the Binary-coded decimal representation of VX, with the most significant of three digits at the address in I, the middle digit at I plus 1, and the least significant digit at I plus 2. (In other words, take the decimal representation of VX, place the hundreds digit in memory at location in I, the tens digit at location I+1, and the ones digit at location I+2.)')
    elif (x & 0x00FF) == 0x0055:
      print(hex(x), 'FX55 Stores V0 to VX in memory starting at address I.')
    elif (x & 0x00FF) == 0x0065:
      print(hex(x), 'FX65 Fills V0 to VX with values from memory starting at address I.')
    else:
      print(hex(x), 'Not Handled yet!')

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

  def interpretOpcode(x):
      if (x & 0xF000) not in interpreter.OpcodePrefix:
          OpcodeDoesNotExist()
      else:
          interpreter.OpcodePrefix[x & 0xF000](x)
          # OpcodePrefix[x & 0xF000](str(x))

  def OpcodeDoesNotExist():
      print('This opcode does not exist')

  def GetOpcodeAddressNNN(x):
      return hex(0x0FFF & int(x))


def Main():
    interpreter.interpretOpcode(0x3522)

if __name__=='__main__':
    Main()