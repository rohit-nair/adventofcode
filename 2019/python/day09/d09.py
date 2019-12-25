#! /usr/bin/env python3

from ..day05.intCode import Processor
from os import path

def get_input(file='testinput09.txt'):
  with open(path.join(path.dirname(__file__), file), 'r+') as f:
    return list(map(int, f.readline().rstrip('\r').rstrip('\n').split(',')))

p = Processor(get_input('input09.txt'), (x for x in [2]))
print(f'Result: {list(p.process())}')