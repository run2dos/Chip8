from nose.tools import *
from Chip8.Opcode_interpreter import interpretOpcode


def test_zero_series_opcode():
    test = interpretOpcode(0x00EE)
    

