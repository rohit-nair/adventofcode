#! /usr/env/bin python3

from ..day05.intCode import Processor
from os import path

UP = -1
DOWN = 1
g = None

NORTH = 0
SOUTH = 1
EAST  = 2
WEST  = 3

class GameOfLife:
  def __init__(self, grid):
    self.g = [grid]
    self.base_lvl = 0
    self.height, self.width = len(self.g[0]), len(self.g[0][1])

  def simulate(self, simulations=10):
    self.scores = [self.get_score(0)]
    for _ in range(simulations):
      # Step 1, Add a new layer on top and bottom
      self.g.insert(0, self.get_empty_grid())
      self.g.append(self.get_empty_grid())
      self.scores.insert(0, 0)
      self.scores.append(0)
      self.base_lvl += 1

      # Step 2: Let them all mutate
      bug_count = [[[self.count_bugs(x, y, idx) for x in range(self.width)] 
        for y in range(self.height)] 
        for idx, grid in enumerate(self.g)]

      g_ = [[[self.mutate(self.g[idx][y][x], bug_count[idx][y][x]) for x in range(self.width)] 
        for y in range(self.height)]
        for idx, grid in enumerate(self.g)]
      self.g = g_

      # Step 3: Get bug counts on each layer
      self.scores = [self.get_score(i) for i in range(len(self.g))]

      # Step 4: Remove top/bottom layer if no bugs found 
      # and update base level if needed
      if self.scores[0] == 0:
        # remove top layer as it hasn't infestated
        del self.g[0]
        self.base_lvl -= 1
      if self.scores[-1] == 0:
        # remove bottom layer as it hasn't infestated
        self.g.pop()
    
    return sum(self.scores)
  
  def get_empty_grid(self):
    return [[0 for x in range(self.width)] for y in range(self.height)]

  def mutate(self, state, bugs):
    if state:
      return 1 if bugs == 1 else 0
    else:
      return 1 if bugs in (1, 2) else 0

  def print_grid(self, grids, as_is=False):
    for i, grid in enumerate(grids):
      print(f'Level: {i - self.base_lvl}')
      for y, r in enumerate(grid):
        print(''.join(['?' if x == 2 and y == 2 else str(c) if as_is else '#' if c else '.' for x, c in enumerate(r)]))

      print('xxxxxxxxxxxxxxxxxxxxxxxxxxx')

  def count_bugs(self, x, y, lvl):
    return sum(map(lambda d: self.get_value(x+d[0], y+d[1], d[2], lvl),
      [(0, -1, NORTH), (0, 1, SOUTH), (-1, 0, EAST), (1, 0, WEST)]))

  def get_value(self, x, y, orient, lvl):
    if y < 0 or y >= self.height or x < 0 or x >= self.width:
      # go one level UP
      if lvl == 0:
        # on top level
        return 0
      elif x < 0:
        return self.g[lvl + UP][2][1]
      elif y < 0:
        return self.g[lvl + UP][1][2]
      elif x == self.width:
        return self.g[lvl + UP][2][3]
      elif y == self.height:
        return self.g[lvl + UP][3][2]
      else:
        raise Exception('Invalid operation')
    elif x == 2 and y == 2:
      # go one level DOWN
      if lvl + 1 == len(self.g):
        # on bottom layer
        return 0
      elif orient == NORTH:
        return sum(self.g[lvl + DOWN][-1])
      elif orient == SOUTH:
        return sum(self.g[lvl + DOWN][0])
      elif orient == EAST:
        return sum([self.g[lvl + DOWN][j][-1] for j in range(self.height)])
      elif orient == WEST:
        return sum([self.g[lvl + DOWN][j][0] for j in range(self.height)])
      else:
        raise Exception('Invalid operation')
    else:
      return self.g[lvl][y][x]

  def get_score(self, lvl):
    return sum([0 if x==2 and y==2 else self.g[lvl][y][x] for y in range(self.height) for x in range(self.width)])


if __name__ == '__main__':
  with open(path.join(path.dirname(__file__), 'input24.txt'), 'r+') as f:
    states = [[1 if c == '#' else 0 for c in l.strip()] for l in f.readlines()]
    g = GameOfLife(states)

    val = g.simulate(200)
    print(f'Biodiversity Rating: {val}')