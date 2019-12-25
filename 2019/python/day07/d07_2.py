#! /usr/bin/env python3

from ..day05.d05 import compute

def execute():
  res, phases = float('-inf'), set(range(5, 10))

  for a in phases:
    for b in phases - set([a]):
      for c in phases - set([a,b]):
        for d in phases - set([a,b,c]):
          for e in phases - set([a,b,c,d]):
            candidate = amplify([a,b,c,d,e])
            if candidate[0] > res:
              res = candidate[0]
  return res

def amplify(phases):
  inputs = [0]
  for i in range(5):
    program = act_input.copy()
    inputs.insert(0, phases[i])
    inputs = compute(program, inputs)
    print(f'Phase: {phases} | Run {i} | Output: {inputs}')
  return inputs



def get_input(file='testinput.txt'):
  with open(file, 'r+') as f:
    # print(f.readline().split(','))
    return [int(x) for x in f.readline().rstrip('\r').rstrip('\n').split(',')]

act_input = get_input('2019/python/day07/input07.txt')
print(f'Max output: {execute()}')
