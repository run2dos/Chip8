"""Loads rom into Memory"""

romName = 'BLINKY.ch8'

romLocation = '/Volumes/Macintosh HD/Users/HGHRLLR/Python/projects/Chip8/rom/' + romName

 
f = open(romLocation, 'r')
rom = f.read()
rom = rom.replace(' ', '').replace('\n', '')
_str = ''
for idx, _byte in enumerate(rom):
    if len(_str) == 2:
        print(_str)
        _str = ''
    else:
        _str += _byte
f.close()

