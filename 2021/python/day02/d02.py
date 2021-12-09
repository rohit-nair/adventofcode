#! /usr/bin/env python3

from functools import reduce
import math
from operator import add
from os import path
from typing import Callable, NamedTuple

class Navigation(NamedTuple):
  index: int
  multiple: int
  aim: Callable[[int, list], int]

# Direction and a tuple of the form (index, multiple, func)
NAVIGATION = {
  'forward': Navigation(0, 1, lambda steps, coordinates: [steps, coordinates[AIM]*steps, 0]),
  'down': Navigation(1, 1, lambda steps, _: [0, 0, steps]),
  'up': Navigation(1, -1, lambda steps, _: [0, 0, -steps])
}

DIRECTION, STEPS, AIM = 0, 1, 2

def multiply(items):
  # return math.prod(items)
  return reduce(lambda x, y: x*y, items)

def execute():
  # [Horizontal, Vertical, Aim]
  coordinates = [0, 0, 0]
  with open(path.join(path.dirname(__file__), 'input02.txt'), 'r+') as f:
    for l in f.readlines():
      directions = l.strip().split(' ')
      nav = NAVIGATION[directions[DIRECTION]]
      steps = int(directions[STEPS])
      # coordinates[nav.index] += nav.multiple * steps
      coordinates = list(map(add, coordinates, nav.aim(steps, coordinates)))

  print(f'Final coordinate is {coordinates}. Result: {multiply(coordinates[:2])}')

if __name__ == '__main__':
  execute()