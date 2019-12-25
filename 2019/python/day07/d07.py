#! /usr/bin/env python3
import itertools
from os import path

from ..day05.intCode import Processor

def execute():
  res = float('-inf')

  for a in itertools.permutations(range(5)):
    candidate = amplify(a)
    if candidate[0] > res:
      res = candidate[0]
  return res

def amplify(phases):
  inputs = [0]
  for i in range(5):
    program = act_input.copy()
    inputs.insert(0, phases[i])
    p = Processor(program, iter(inputs))
    inputs = list(p.process())
  return inputs

def get_input(file='testinput07.txt'):
  with open(path.join(path.dirname(__file__), file), 'r+') as f:
    return [int(x) for x in f.readline().rstrip('\r').rstrip('\n').split(',')]

if __name__ == '__main__':
  act_input = get_input('input07.txt')
  print(f'Max output: {execute()}')
