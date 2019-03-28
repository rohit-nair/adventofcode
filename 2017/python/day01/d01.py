#! /usr/bin/env python3

import os

def readInput(p):
  with open('input01.txt', 'r+') as f:
    return f.readline().rstrip('\n')

def process(inputs):
  if len(inputs) == 0:
    return 0
  elif len(inputs) == 1:
    return int(inputs)

  s, icrm = 0, int(len(inputs)/2)
  mod_input = inputs + inputs
  print(s, icrm)
  for i in range(len(inputs)):
    s += int(inputs[i]) if mod_input[i+icrm] == inputs[i] else 0

  return s



if __name__ == "__main__":
  # assert 3 == process('1122'), 'Woopsies 1.'
  # assert 4 == process('1111'), 'Woopsies 2.'
  # assert 0 == process('1234'), 'Woopsies 3.'
  # assert 9 == process('91212129'), 'Woopsies 4.'

  actual_inputs = readInput('input01.txt')
  print("Result: {0}".format(process(actual_inputs)))