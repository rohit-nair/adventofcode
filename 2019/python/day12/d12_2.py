#! /usr/bin/env python3

from math import gcd
import numpy as np
import pandas as pd
from os import path
import re

INPUT_PATTERN = r"<.=(\-?\d+), .=(\-?\d+), .=(\-?\d+)>"

def simulate(position, velocity):
  repeat_occurences = [0] * len(position[0])
  for dim in range(len(position[0])):
    init_x, init_v = np.array([row[dim] for row in position]), np.array([row[dim] for row in velocity])
    i, x, v, = 1, init_x.copy(), init_v.copy()
    while True:
      less_than, greater_than = np.array([sum(x < p) for p in x]), np.array([sum(x > p) for p in x])
      gravity = np.array(greater_than - less_than)
      v += gravity
      x += v
      if (x == init_x).all() and (v == init_v).all():
        repeat_occurences[dim] = i
        break
      i += 1
  print(repeat_occurences, np.prod(repeat_occurences))

  return find_lcm(repeat_occurences)

def find_lcm(values):
  lcm = values[0]
  for i in values[1:]:
    lcm = lcm*i // gcd(lcm, i)
  return lcm

def get_inputs(file='testinput12.txt'):
  position, velocity = [], []
  with open(path.join(path.dirname(__file__),file), 'r+') as f:
    for l in f.readlines():
      matches = re.match(INPUT_PATTERN, l.rstrip('\r').rstrip('\n'))
      position.append(list(map(int, matches.groups())))
      velocity.append([0, 0, 0])
  return position, velocity

if __name__ == '__main__':
  print(simulate(*get_inputs('input12.txt')))
  # assert simulate(*get_inputs()) == 4686774924, 'Assertion failed.'
