#! /usr/env/bin python3

from ..day05.intCode import Processor
from collections import deque
from os import path

if __name__ == '__main__':
  with open(path.join(path.dirname(__file__), 'input25.txt'), 'r+') as f:
    code = [int(x) for x in f.readline().strip().split(',')]
    p = Processor(code, [])
    res = p.process()
    while True:
      val = next(res) 
      if val:
        print(chr(val), end='')
      else:
        inp = input('')
        inp_ascii = [ord(c) for c in inp] + [10]
        for i in inp_ascii:
          p.add_input(i)

# hologram, space law space brochure, spool of cat6, space heater