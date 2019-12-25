#! /usr/bin/env python3

import asyncio
from ..day05.intCode import Processor
from os import path

def is_affected_region(x, y):
  if x < 0 or y < 0:
    return 0
  return next(Processor(code.copy(), [x,y]).process())

if __name__ == '__main__':
  with open(path.join(path.dirname(__file__), 'input19.txt'), 'r+') as f:
    code = [int(x) for x in f.readline().strip().split(',')]

    affected = 0
    for y in range(50):
      for x in range(50):
        res = is_affected_region(x,y)
        affected += res

    print(f'Affected region: {affected}')

    size = 100
    x, y = 0, 1
    # Cells o test before deciding no
    # affected region in row
    win_width = 15

    while True:
      print(x, y)
      left_x = -1
      for i in range(-win_width, win_width):
        if is_affected_region(x+i,y):
          left_x = x+i
          break
      
      # Assume no affected region in this row
      if left_x == -1:
        print(f'No affected region found')
        y += 1
        continue

      x = left_x
      
      # Affected region not wide enough
      if not is_affected_region(left_x+size-1, y):
        y += 1
        continue

      if not is_affected_region(left_x, y-size+1):
        y += 1
        continue

      if not is_affected_region(left_x+size-1, y-size+1):
        y += 1
        continue

      # Found closest region to fit Santa's ship
      print(f'Locator value:{left_x*(size**2) + y - size + 1}')
      break