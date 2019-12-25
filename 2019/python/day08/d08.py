#! /usr/bin/env python3
from math import inf

BLACK, WHITE, TRAN = 0, 1, 2

def compute(nums, columns, rows):
  dfs = [c for c in get_chunks(nums, columns*rows)]
  
  min_0s, res = inf, 0
  for c in dfs:
    counts = list(map(lambda x: c.count(x), [0,1,2]))
    if min_0s > counts[0]:
      min_0s = counts[0]
      res = counts[1]*counts[2]
  
  print(f'Checksum: {res}')
  
  img = [[None for x in range(columns)] for y in range(rows)]
  for x in range(columns):
    for y in range(rows):
      for c in dfs:
        val = c[y*columns+x]
        if not val == TRAN:
          img[y][x] = ' ' if val == BLACK else '#'
          break
  
  for r in img:
    print(' '.join(r))


def get_chunks(nums, size):
  for i in range(0, len(nums), size):
    yield nums[i:i+size]


def get_input(file='2019/python/day08/input08.txt'):
  with open(file, 'r+') as f:
    # print(f.readline().split(','))
    return list(map(int, list(f.readline().rstrip('\r').rstrip('\n'))))

print(f'Checksum: {compute(get_input(), 25, 6)}')