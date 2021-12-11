#! /usr/bin/env python3

from collections import deque
from os import path

PUSES = None

def p1():
  get_input()
  flashes, step = 0, 1
  while True:
    flashes += execute_step()
    if all_flashed():
      break
    step += 1

  print(f'Number of flashes after 100 step was {flashes}.')
  print(f'All octopuses flashed on step {step}.')

def all_flashed():
  return not any([c for r in PUSES for c in r])

def execute_step():
  height, width = len(PUSES), len(PUSES[0])
  # Contains tuple coordinates
  seen = set()
  flashes = 0

  full_puses = set()

  for y in range(len(PUSES)):
    for x in range(len(PUSES[0])):
      if PUSES[y][x] == 9:
        flashes += 1
        PUSES[y][x] = 0
        full_puses.add((x, y))
      else:
        PUSES[y][x] += 1

  for x, y in full_puses:
    if (x, y) in seen:
      continue

    seen.add((x, y))

    coord = {(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)}
    ripple = deque([(x+dx, y+dy) for dx, dy in coord])

    while ripple:
      xx, yy = ripple.popleft()
      if (xx, yy) in seen:
        continue

      if not ((0 <= xx < width) and (0 <= yy < height)):
        continue

      if PUSES[yy][xx] == 9:
        PUSES[yy][xx] = 0
        flashes += 1
        ripple.extendleft([(xx+dx, yy+dy) for dx, dy in coord])
        seen.add((xx, yy))
      elif (xx, yy) not in full_puses:
        PUSES[yy][xx] += 1

  return flashes





def print_puses():
  for row in PUSES:
    print(''.join(map(str,row)))
  print()

def get_input():
  global PUSES
  with open(path.dirname(__file__) + '/input11.txt') as f:
    PUSES = [list(map(int, list(l.strip()))) for l in f.readlines()]

p1()