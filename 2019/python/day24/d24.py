#! /usr/env/bin python3

from ..day05.intCode import Processor
from os import path

UP = -1
DOWN = 1
g = None

class GameOfLife:
  def __init__(self, grid):
    self.g = grid
    self.height, self.width = len(self.g), len(self.g[0])

  def simulate(self):
    scores = [self.get_score()]
    while True:
      bug_count = [[self.count_bugs(x, y) for x in range(self.width)] for y in range(self.height)]
      g_ = [[self.mutate(self.g[y][x], bug_count[y][x]) for x in range(self.width)] for y in range(self.height)]
      self.g = g_
      score = self.get_score()
      if score in scores:
        return score
      scores.append(score)

  def mutate(self, state, bugs):
    if state:
      return 1 if bugs == 1 else 0
    else:
      return 1 if bugs in (1, 2) else 0

  def print_grid(self, as_is=False):
    for r in self.g:
      print(''.join([str(c) if as_is else '#' if c else '.' for c in r]))

  def count_bugs(self, x, y):
    return sum(map(lambda d: self.get_value(x+d[0], y+d[1]), [(-1,0), (0, -1), (1, 0), (0, 1)]))

  def get_value(self, x, y):
    if y < 0 or y >= self.height or x < 0 or x >= self.width:
      return 0
    return self.g[y][x]

  def get_score(self):
    return sum([self.g[y][x] * (2**(y*self.width+x)) for y in range(self.height) for x in range(self.width)])


if __name__ == '__main__':
  with open(path.join(path.dirname(__file__), 'input24.txt'), 'r+') as f:
    states = [[1 if c == '#' else 0 for c in l.strip()] for l in f.readlines()]
    g = GameOfLife(states)

    val = g.simulate()
    print(f'Biodiversity Rating: {val}')