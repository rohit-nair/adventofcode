#!/usr/bin/env python
import re, string, operator
from collections import defaultdict

def getinput(file='testinput.txt'):
  with open(file, 'r+') as f:
    return [tuple(map(int, l.rstrip('\n').split(', '))) for l in f.readlines()]

def getspace(input, leyway=1):
  mx, my = max([x[0] for x in input]), max([x[1] for x in input])
  return [[findclosestcoord(input, (x, y)) for x in range(mx+leyway)] for y in range(my+leyway)]

def getspacebydistacetocoords(input, leyway=1):
  mx, my = max([x[0] for x in input]), max([x[1] for x in input])
  return [[finddistancefromallcoord(input, (x, y)) for x in range(mx+leyway)] for y in range(my+leyway)]

def finddistancefromallcoord(input, p):
  return sum([getmanhattandistance(x, p) for x in input])

def findclosestcoord(input, p):
  if p in input:
    return input.index(p)

  m = min([getmanhattandistance(x, p) for x in input])
  midxs = [i for i, x in enumerate(input) if getmanhattandistance(x, p) == m]
  # print(m, p, midxs)
  return '#' if len(midxs) > 1 else midxs[0]

def getmanhattandistance(p1, p2):
  # print(p1,p2)
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def getremotepoint(file='testinput.txt'):
  input = getinput(file)
  s = getspace(input)
  # print(s)
  mx, my, extremes, coords, area = len(s[0]), len(s), set(), set([range(len(input))]), defaultdict(int)
  for y in range(my):
    for x in range(mx):
      # remove coordinates in extreeme ends
      if y in (0, my-1) or x in (0, mx-1):
        extremes.add(s[y][x])
      area[s[y][x]] += 1
  
  return max({k: v for k,v in area.items() if k not in extremes}.items(), key=operator.itemgetter(1))

def getsnugpoints(file='testinput.txt', maxdist = 32):
  input = getinput(file)
  s = getspacebydistacetocoords(input, 0)
  return sum([1 for r in s for c in r if c < maxdist])



# print(getremotepoint('input.txt'))
print(getsnugpoints('input.txt', 10000))