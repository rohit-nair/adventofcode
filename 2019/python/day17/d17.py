#! /usr/bin/env python3

from ..day05.intCode import Processor
from os import path

NORTH       = '^'
SOUTH       = 'v'
WEST        = '>'
EAST        = '<'

SPACE       = '.'
SCAFFOLDING = '#'

ORIENTATION = {
  NORTH     : 1,
  SOUTH     : 2,
  WEST      : 3,
  EAST      : 4
}

def start(inputs):
  p = Processor(inp, [])
  gen = p.process()
  x, y = -1, -1
  i = 0
  input_processed = False

  while True:
    try:
      x, y = len(grid[-1]), len(grid) - 1
      val = next(gen)
      c = chr(val)
      if input_processed:
        continue
      if c == '\n':
        grid.append([])
        continue
      else:
        grid[-1].append(c)
        if c == SCAFFOLDING:
          intersection = is_cell_above_intersection(grid, (x, y))
          if intersection:
            intersections.append((x,y-1))

      if c in ORIENTATION:
        droid_x, droid_y, droid_orient = x, y, c
        assert get_value(grid, (x,y)) == c, 'Droid locator logic failed'

    except Exception as e:
      input_processed = True
      if i < len(inputs):
        for val in inputs[i]:
          p.add_input(val)
        i += 1
      else:
        break
      pass
  return val

def is_cell_above_intersection(g, pos):
  intersection_cells = [(0, 0), (0, -1), (0, -2), (-1, -1), (1, -1)]
  vals = [SCAFFOLDING == get_value(g, tuple(map(sum, zip(pos,c)))) for c in intersection_cells]
  return all(vals)

def is_intersection(g, pos):
  intersection_cells = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
  vals = [SCAFFOLDING == get_value(g, tuple(map(sum, zip(pos,c)))) for c in intersection_cells]
  return all(vals)

def get_value(g, pos):
  if not (0 <= pos[0] < len(g[0]) and 0 <= pos[1] < len(g)):
    return None
  return g[pos[1]][pos[0]]

def print_grid(g):
  for r in g:
    print(''.join(r))

def convert_to_ascii(val):
  return [ord(c) for c in val]

if __name__ == '__main__':
  with open(path.join(path.dirname(__file__), 'input17.txt'), 'r+') as f:
    grid = [[]]
    droid_x, droid_y, droid_orient = -1, -1, 1
    intersections = []
    inp = [int(x) for x in f.readline().strip().split(',')]
    inp[0] = 2

    main_input = convert_to_ascii('A,B,A,B,C,C,B,A,B,C\n')
    A = convert_to_ascii('L,12,L,10,R,8,L,12\n')
    B = convert_to_ascii('R,8,R,10,R,12\n')
    C = convert_to_ascii('L,10,R,12,R,8\n')
    video = convert_to_ascii('n\n')
    all_inputs = [main_input, A, B, C, video]

    dust_count = start(all_inputs)

    print(f'# of intersections: {sum([a*b for a,b in intersections])}')
    print(f'Number of dust particles collected: {dust_count}')

