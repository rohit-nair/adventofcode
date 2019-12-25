#!/usr/bin/env python3
from collections import namedtuple
import math
from os import path
import sys

Point = namedtuple('Point', ['x', 'y'])

class AsteroidField:
  def __init__(self, asteroids):
    self.asteroids = asteroids

  def find_vantage_point(self):
    max_visible_asteroids, vantage_point = 0, None
    foo = {}
    for a in self.asteroids:
      visible_asteroids = self._find_visible_asteroids(a)
      # foo[a] = visible_asteroids
      if visible_asteroids > max_visible_asteroids:
        max_visible_asteroids = visible_asteroids
        vantage_point = a
    # return foo
    return vantage_point, max_visible_asteroids

  def _find_visible_asteroids(self, a):
    visible_asteroids = 0
    for b in (self.asteroids - set([a])):
      is_hidden = False
      for c in (self.asteroids - set([a, b])):
        if is_between(a, b, c):
          is_hidden = True
          break
      if not is_hidden:
        visible_asteroids += 1
    return visible_asteroids


def distance(a,b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

def is_between(a,b,c):
  return -0.00000001 < (distance(a, c) + distance(c, b) - distance(a, b)) < 0.00000001

def get_asteroids(file='testinput10.txt'):
  with open(path.join(path.dirname(__file__), file), 'r+') as f:
    asteroids = set()
    for y, l in enumerate(f.readlines()):
      for x, c in enumerate(l.rstrip('\r').rstrip('\n')):
        if c == '#':
          asteroids.add(Point(x, y))

    return asteroids


af = AsteroidField(get_asteroids())
res = af.find_vantage_point()
assert res[1] == 210, 'Assertion failed.'

# af = AsteroidField(get_asteroids('input10.txt'))
# point, counts = af.find_vantage_point()
# print(point, counts)
# grid = [list('.....') for _ in range(5)]
# for p, v in res.items():
#   grid[p.y][p.x] = str(v)
# for r in grid:
#   print(''.join(r)) 

# assert is_between(Point(1,0), Point(3,4), Point(2, 2)) == True, 'Assertion failed.'
# assert af._find_visible_asteroids(Point(1,0)) == 7, 'Assertion 2 failed.'