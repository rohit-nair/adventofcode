#! /usr/bin/env python3

import os
from typing import NamedTuple

class Coordinates(NamedTuple):
  x: int
  y: int

NO_VENTS = '.'

def process():
  vents, width, depth = get_input()
  
  ocean = [[NO_VENTS]*width for y in range(depth)]
  more_than_1_vents = plot_vents(vents, ocean)
  # print_ocean(ocean)
  print(f"{more_than_1_vents} points have at least two lines overlapping.")
  # count_max_vents(ocean, max_vents)

def count_max_vents(ocean, max_vents):
  cnt = 0
  for row in ocean:
    cnt += sum([r==max_vents for r in row])

  return cnt

def plot_vents(vents, ocean):
  more_than_1_vents = 0
  for coord_1, coord_2 in vents:

    # Vertical vents
    if coord_1.x == coord_2.x:
      # print(f'Vertical {coord_1, coord_2}')
      min_y, max_y = min(coord_1.y, coord_2.y), max(coord_1.y, coord_2.y)
      y = min_y
      while y <= max_y:
        current_state = ocean[y][coord_1.x] 
        updated_state = 1 if current_state == NO_VENTS else current_state + 1
        ocean[y][coord_1.x] = updated_state
        if updated_state == 2:
          more_than_1_vents += 1
        y += 1

    # Horizontal vents
    if coord_1.y == coord_2.y:
      # print(f'Horizontal {coord_1, coord_2}')
      min_x, max_x = min(coord_1.x, coord_2.x), max(coord_1.x, coord_2.x)
      x = min_x
      while x <= max_x:
        current_state = ocean[coord_1.y][x] 
        updated_state = 1 if current_state == NO_VENTS else current_state + 1
        ocean[coord_1.y][x] = updated_state
        if updated_state == 2:
          more_than_1_vents += 1
        x += 1

    # Diagonal vents
    if abs(coord_1.x - coord_1.y) == abs(coord_2.x - coord_2.y) or abs(coord_1.x + coord_1.y) == abs(coord_2.x + coord_2.y):
      # print(f'Diagonal {coord_1, coord_2}')
      start, end = (coord_1, coord_2) if coord_1.x < coord_2.x else (coord_2, coord_1)
      step_y = 1 if start.y < end.y else -1
      x, y = start
      while x <= end.x:
        current_state = ocean[y][x]
        updated_state = 1 if current_state == NO_VENTS else current_state + 1
        # print(x, y, current_state, updated_state)
        ocean[y][x] = updated_state
        if updated_state == 2:
          more_than_1_vents += 1
        x += 1
        y += step_y
  
  return more_than_1_vents



def print_ocean(ocean):
  for row in ocean:
    print(''.join([str(r) for r in row]))

def get_input():
  width, depth = 0, 0
  with open(os.path.dirname(__file__) + '/input05.txt', 'r+') as f:
    vents = []
    for l in f.readlines():
      coords = [Coordinates(*list(map(int, c.split(',')))) for c in l.strip().split(' -> ')]
      vents.append(coords)
      width, depth = max(width, coords[0][0], coords[1][0]), max(depth, coords[0][1], coords[1][1])

    return vents, width+1, depth+1

process()