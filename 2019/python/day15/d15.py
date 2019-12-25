#! /usr/bin/env python3

import curses
from collections import deque
from ..day05.intCode import Processor
from math import inf
from os import path
import random
import time

NORTH     = 1
SOUTH     = 2
WEST      = 3
EAST      = 4

WALL      = 0
MOVED     = 1
O2        = 2
DROID     = 99
PATH      = 98

SYMBOLS = {
  WALL    : '#',
  MOVED   : '.',
  DROID   : '@',
  O2      : '0',
  PATH    : '*'
}

EOM = 'End of Minute'

def start(w, program):
  p = Processor(program,[])
  gen = p.process()
  cells = {(0,0):MOVED}
  min_x,min_y,max_x,max_y = 0,0,0,0
  x,y = 0,0
  o2_x, o2_y = -inf, -inf
  found_o2 = False
  counter = 0
  try:
    while True: 
      counter += 1
      if found_o2 and abs(x) < 2 and abs(y) < 2:
        break

      # Find valid move
      next_x, next_y, move = find_valid_move(cells, x, y)

      p.add_input(move)
      res = next(gen)

      if res == MOVED:
        cells[(next_x, next_y)] = MOVED
      elif res == WALL:
        cells[(next_x, next_y)] = WALL
        min_x, min_y, max_x, max_y = min(next_x, min_x), min(next_y, min_y), max(next_x, max_x), max(next_y, max_y)
        continue
      elif res == O2:
        if not found_o2:
          cells[(next_x, next_y)] = O2
          o2_x, o2_y = next_x, next_y
          found_o2 = True
      x, y = next_x, next_y
      min_x, min_y, max_x, max_y = min(x, min_x), min(y, min_y), max(x, max_x), max(y, max_y)
  except StopIteration as e:
    pass

  route = find_optimal_route(cells, (o2_x, o2_y))
  time_to_fill = fill_oxygen(w, cells, (o2_x,o2_y))

  return len(route) + 1, time_to_fill

def find_optimal_route(cells, o2):
  q = deque([(o2, [])])
  found_origin = False

  while q:
    (x, y), route = q.popleft()
    for move in range(1, 5):
      next_x = x + (None, 0, 0, 1, -1)[move]
      next_y = y + (None, 1, -1, 0, 0)[move]

      if (next_x, next_y) == (0,0):
        found_origin = True
        break

      if (next_x, next_y) in cells and cells[(next_x, next_y)] != WALL and (next_x, next_y) not in route:
        q.append(((next_x, next_y), route + [(x,y)]))

    if found_origin:
      break

  for x,y in route:
    if (x,y) != o2:
      cells[(x,y)] = PATH

  return route

def fill_oxygen(w, cells, o2):
  q = deque([o2, EOM])
  found_origin = False
  minutes = 0
  min_x, min_y, max_x, max_y = min([x[0] for x in cells.keys()]), \
    min([x[1] for x in cells.keys()]), \
    max([x[0] for x in cells.keys()]), \
    max([x[1] for x in cells.keys()])

  while q:
    item = q.popleft()
    if item == EOM:
      if len(q) == 0:
        break
      q.append(EOM)
      minutes += 1
      continue

    x,y = item
    for move in range(1, 5):
      next_x = x + (None, 0, 0, 1, -1)[move]
      next_y = y + (None, 1, -1, 0, 0)[move]

      if (next_x, next_y) in cells and cells[(next_x, next_y)] not in (WALL, O2):
        q.append((next_x, next_y))
    
    cells[(x,y)] = O2

  return minutes

def find_valid_move(cells, x, y):
  candiate_moves = []
  found_move = False
  for move in range(1, 5):
    next_x = x + (None, 0, 0, 1, -1)[move]
    next_y = y + (None, 1, -1, 0, 0)[move]
    if (next_x, next_y) not in cells:
      found_move = True
      break
    elif cells[(next_x, next_y)] != WALL:
      candiate_moves.append((next_x, next_y, move))
  
  if not found_move:
    return candiate_moves[random.randint(0, len(candiate_moves) - 1)]

  return next_x, next_y, move
  

def draw_screen(w, cells, min_x, min_y, max_x, max_y, x, y):
  curses.start_color()
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
  w.clear()
  w.refresh()
  screen = [[' ' for r in range(max_x-min_x+1)] for c in range(max_y-min_y+1)]
  blocks = 0
  # print(cells)
  try:
    for (i, j), tile_id in cells.items():
      screen[j-min_y][i-min_x] = 'X' if (i,j) == (0,0) else SYMBOLS[DROID] if (i,j) == (x,y) else SYMBOLS[tile_id]

    for r in screen:
      for c in r:
        if c in (SYMBOLS[PATH], SYMBOLS[O2]):
          w.addstr(c, curses.color_pair(1))
        else:
          w.addstr(c)
      w.addch('\n')
  except Exception as e:
    pass

  w.refresh()


def get_input(file='input15.txt'):
  with open(path.join(path.dirname(__file__), file), 'r+') as f:
    return [int(x) for x in f.readline().strip().split(',')]


if __name__ == '__main__':
  code = get_input()
  min_dist_o2, time_to_fill = curses.wrapper(start, code)
  print(f'Min distance to oxygen: {min_dist_o2} and time to fill oxygen: {time_to_fill}')