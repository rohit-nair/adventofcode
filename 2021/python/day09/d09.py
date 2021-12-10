#! /usr/bin/env python3

from collections import deque
from functools import reduce
from operator import mul
from os import path
from typing import Deque, NamedTuple

MAP = []

class Point(NamedTuple):
  x: int
  y: int
  val: int

def process():
  global MAP
  MAP = get_input()

  lowest_points, risk = get_risk()
  print(f'Risk score for the map is {risk}.')

  res = find_basins(lowest_points)
  print(f'Product of sizes of all basin is {res}.')


def find_basins(lowest_points):
  global MAPPED_TERRITORY
  MAPPED_TERRITORY = [[False]*len(MAP[0]) for _ in range(len(MAP))]
  basin_sizes = [find_basin_size(p) for p in lowest_points]
  return reduce(mul, sorted(basin_sizes, reverse=True)[:3])


def find_basin_size(lo: Point):
  global MAPPED_TERRITORY
  width, height = len(MAP[0]), len(MAP)
  q, size = deque([lo]), 0
  while len(q) > 0:
    # print(q, len(q))
    p = q.popleft()
    if not has_already_mapped(p) and p.val != 9:
      size += 1

      if p.x != 0:
        val = MAP[p.y][p.x-1]
        if val != 9:
          q.append(Point(p.x-1, p.y, val))
      if p.x != width - 1:
        val = MAP[p.y][p.x+1]
        if val != 9:
          q.append(Point(p.x+1, p.y, val))
      if p.y != 0:
        val = MAP[p.y-1][p.x]
        if val != 9:
          q.append(Point(p.x, p.y-1, val))
      if p.y != height - 1:
        val = MAP[p.y+1][p.x]
        if val != 9:
          q.append(Point(p.x, p.y+1, val))

    MAPPED_TERRITORY[p.y][p.x] = True

  print(f'Size of basin at {p} is {size}.')
  return size


def has_already_mapped(p: Point):
  return MAPPED_TERRITORY[p.y][p.x]


def get_risk():
  height, width = len(MAP), len(MAP[0])
  lowest_points = []

  for y in range(height):
    for x in range(width):
      p = MAP[y][x]

      # Left
      if x != 0 and MAP[y][x-1] <= p:
        continue

      # Right
      if x != width - 1 and MAP[y][x+1] <= p:
        continue

      # Top
      if y != 0 and MAP[y-1][x] <= p:
        continue

      # Bottom
      if y != height - 1 and MAP[y+1][x] <= p:
        continue

      # if (
      #   (x != 0 and MAP[y][x-1] <= p) or
      #   (x != width - 1 and MAP[y][x+1] <= p) or 
      #   (y != 0 and MAP[y-1][x] <= p) or 
      #   (y != height - 1 and MAP[y+1][x] <= p)
      # ):
      #   continue

      lowest_points.append(Point(x, y, p))

  risk = sum([p.val for p in lowest_points]) + len(lowest_points)
  return lowest_points, risk

def print_map():
  for row in MAP:
    print(''.join(map(str,row)))


def get_input():
  with open(path.dirname(__file__) + '/input09.txt', 'r+') as f:
    return [list(map(int, list(l.strip()))) for l in f.readlines()]

process()
# print_map()