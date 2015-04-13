from nose.tools import *
from Chip8.Chip8 import Chip8


def setup():
    print('Setup')

def teardown():
    print("TEAR DOWN!")


def test_memory_size():
    test_CPU = Chip8()
    assert_equals(len(test_CPU.memory), 4096)

def test_registers_exsists():
    test_CPU = Chip8()
    assert_equals(len(test_CPU.reg_V), 16)

def test_registers_read_write():
    test_CPU = Chip8()
    x = 0
    for i in test_CPU.reg_V:
        test_CPU.reg_V[x] = x
        x+=1

    x = 0x0
    for i in test_CPU.reg_V:    
        assert_equals(test_CPU.reg_V[x], x)
        x+=1


