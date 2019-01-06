#!/usr/bin/env python3

import copy
from enum import Enum

class acre(Enum):
  Open = '.'
  Trees = '|'
  Lumberyard = '#'
  OutOfBound = '0'

def getinput(file='testinput18.txt'):
  with open(file, 'r+') as f:
    return [list(l.rstrip('\n')) for l in f.readlines()]

def iterate(state, times=10):
  pprint(state)
  for i in range(times):
    newstate = copy.deepcopy(state)
    for y in range(1, len(state) - 1):
      for x in range(1, len(state[0]) - 1):
        # print(x, y)
        newstate[y][x] = getcellstate([c \
          for k, r in enumerate(state[y-1:y+2]) \
            for l, c in enumerate(r[x-1:x+2])])
    state = copy.deepcopy(newstate)
  pprint(state)
  return state

def getcellstate(neighbours):
  assert len(neighbours) <= 9, "Neighbours passed should be less than 10."
  curcell = neighbours[4]

  if curcell == acre.Open.value:
    return acre.Trees.value if neighbours.count(acre.Trees.value) > 2 else curcell
  
  if curcell == acre.Trees.value:
    return acre.Lumberyard.value if neighbours.count(acre.Lumberyard.value) > 2 else curcell

  if curcell == acre.Lumberyard.value:
    return curcell if neighbours.count(acre.Lumberyard.value) > 1 and neighbours.count(acre.Trees.value) > 0 else acre.Open.value

def addpadding(state, nbrofpadding):
  newstate = [[acre.OutOfBound.value]*nbrofpadding + r + [acre.OutOfBound.value]*nbrofpadding for r in state]
  return [[acre.OutOfBound.value]*len(newstate[0])]*nbrofpadding + newstate + [[acre.OutOfBound.value]*len(newstate[0])]*nbrofpadding

def pprint(s):
  if len(s[0]) == 1:
    print(' '.join(s))
    return 

  for r in s:
    print(' '.join(r))
# s = getinput('input18.txt')
# s = addpadding(s, 1)
# ns = iterate(s)
# print('Resouce value: {}'.format(sum(r.count(acre.Trees.value) for r in ns) * sum(r.count(acre.Lumberyard.value) for r in ns)))

# PART 2
s = getinput('input18.txt')
s = addpadding(s, 1)
# ns = iterate(s, 1000)

# From the above iteration it's found that the resource value stabilizes 
# and the value after 1000 iterations is 189720 hence the value after
# 1000000000 is 189720





##########################
# TESTS
##########################

# print(getcellstate(list('....#||..')))