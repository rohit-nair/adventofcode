#!/usr/bin/env python3

from ..day05.intCode import Processor
from collections import defaultdict, deque, namedtuple
from os import path

Point = namedtuple('Point', ['x', 'y'])

LEFT  = 0
RIGHT = 1

BLACK = 0
WHITE = 1

NORTH = 0
WEST  = 1
SOUTH = 2
EAST  = 3


class Robot:
  def __init__(self, code):
    self.brains = Processor(code, [])
    self.cells = defaultdict(int)
    self.orientation = NORTH

  def start(self):
    unique_cells_painted, x, y, first_run = 0, 0, 0, True
    res = self.brains.process()
    try:
      while True:
        cell_color = self.cells[(x,y)]
        self.brains.add_input(1 if first_run else cell_color)
        paint, rotate = next(res), next(res)
        self.cells[(x,y)] = paint
        self.orientation = (self.orientation + rotate * 2 - 1) % 4
        x += (0, 1, 0, -1)[self.orientation]
        y += (-1, 0, 1, 0)[self.orientation]
    except StopIteration:
      pass
    return len(self.cells.keys())

  def paint(self):
    min_x, min_y, max_x, max_y = 0, 0, 0, 0
    for x, y in self.cells.keys():
      min_x, min_y, max_x, max_y = min(min_x, x), min(min_y, y), max(max_x, x), max(max_y, y)

    width, height = max_x - min_x + 1, max_y - min_y + 1
    grid = [[' ' for i in range(width)] for j in range(height)]

    for x in range(width):
      for y in range(height):
        grid[abs(min_y-y)][abs(min_x-x)] = '#' if self.cells[(x,y)] == 1 else ' '

    for r in grid:
      print(''.join(r))


def get_inputs(file='testinput11.txt'):
  with open(path.join(path.dirname(__file__), file), 'r+') as f:
    return [int(c) for c in f.readline().rstrip('\r').rstrip('\n').split(',') ]

if __name__ == '__main__':
  r = Robot(get_inputs('input11.txt'))
  print(f'Unique cells painted: {r.start()}')
  r.paint()
