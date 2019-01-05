#! /usr/bin/env python

import sys
from enum import Enum
from pprint import pprint
from collections import deque

class states(Enum):
  clay = '#'
  soil = ' '
  water = '~'
  trickle = '|'
  outofbounds = '0'

def getinput(file='testinput17.txt'):
  with open(file, 'r+') as f:
    inputs = [l.rstrip('\n').replace(',', '').replace('..', ':').split() for l in f.readlines()]
  
  coords, minx, maxx, miny, maxy = [], float('inf'), 0, float('inf'), 0
  for a, b in inputs:
    (cord1, range1), (cord2, range2) = a.split('='), b.split('=')

    range1 = map(int, range1.split(':')) if range1.find(':') > -1 else [int(range1)]
    range2 = map(int, range2.split(':')) if range2.find(':') > -1 else [int(range2)]

    if cord1 == 'x':
      minx = min(minx, *range1)
      miny = min(miny, *range2)

      maxx = max(maxx, *range1)
      maxy = max(maxy, *range2)

      coords.append((range1, range2))
    else:
      miny = min(miny, *range1)
      minx = min(minx, *range2)

      maxy = max(maxy, *range1)
      maxx = max(maxx, *range2)

      coords.append((range2, range1))
  
  # stretch left/right 
  minx -= 1
  maxx += 1
  
  print('Minx: {}, Maxx: {}, miny:{}, maxy: {}'.format(minx, maxx, miny, maxy))

  section = [[states.soil.value for x in range(maxx-minx+1)] for y in range(maxy-miny+1)]
  for x, y in coords:
    # conver to exclusive ranges
    x[-1], y[-1] = x[-1]  if len(x) ==  1 else x[-1]+1, y[-1] if len(y) == 1 else y[-1]+1
    for j in range(*([y[0], y[0]+1] if len(y) == 1 else y)):
      for i in range(*([x[0], x[0]+1] if len(x) == 1 else x)):
        section[j-miny][i-minx] = states.clay.value
  
  return section, minx, maxx, miny, maxy

def printsection(section):
  for i, r in enumerate(section):
    print('{:0>4d}{}'.format(i, ''.join(r)))
    if i % 50 == 0:
      raw_input('Press any key to continue...\n')

def setcellvalue(x, y, v):
  global section
  if x < 0 or x >= len(section[0]) or y < 0 or y >= len(section):
    return
  
  cellval = states(section[y][x])

  if cellval == states.clay:
    return  # Can't be overwritten
  if cellval == states.water and v == states.trickle.value:
    return  # Can't convert water to trickle
  if cellval == states.trickle and v == states.soil.value:
    return  # Can't convert trickle to soil

  section[y][x] = v

def getcellvalue(x, y):
  global section
  if x < 0 or x >= len(section[0]) or y < 0 or y >= len(section):
    return states.outofbounds
  return states(section[y][x])

def cellisbounded(x, y):
  global section
  belowcellval = getcellvalue(x, y+1)

  return (belowcellval == states.clay or belowcellval == states.water) and \
    cellisboundonleft(x-1, y) and cellisboundonright(x+1, y)

def cellisboundonleft(x, y):
  while True:
    cellval = getcellvalue(x, y)
    belowcellval = getcellvalue(x, y+1)

    if cellval == states.clay:
      return True
    if cellval == states.outofbounds:
      return False
    if belowcellval == states.soil or belowcellval == states.outofbounds:
      return False
    
    x -= 1


def cellisboundonright(x, y):
  while True:
    cellval = getcellvalue(x, y)
    belowcellval = getcellvalue(x, y+1)

    if cellval == states.clay:
      return True
    if cellval == states.outofbounds:
      return False
    if belowcellval == states.soil or belowcellval == states.outofbounds:
      return False
    
    x += 1

def fillrowwithwater(x, y):
  global section
  # Fill water to left
  x_ = x
  while True:
    cellval = getcellvalue(x_, y)
    if cellval == states.clay or cellval == states.outofbounds:
      break
      
    setcellvalue(x_, y, states.water.value)
    x_ -= 1

  # Fill water to right
  x_ = x
  while True:
    cellval = getcellvalue(x_, y)
    if cellval == states.clay or cellval == states.outofbounds:
      break

    setcellvalue(x_, y, states.water.value)
    x_ += 1 

def appendcelltopath(path, x, y):
  if (x, y) not in path:
    path.append((x, y))

def appendleftcelltopath(path, x, y):
  if (x, y) not in path:
    path.appendleft((x, y))

def trickledown(x, y):
  global section
  path, visited = [], []
  path.append((x, y))

  while len(path) > 0:
    # curcell = path.popleft()
    curcell = path.pop()
    cellval = getcellvalue(*curcell)
    x_, y_ = curcell

    belowcellval = getcellvalue(x_, y_+1)

    if cellval == states.water or cellval == states.clay or cellval == states.outofbounds:
      continue

    if belowcellval == states.outofbounds:
      setcellvalue(*(curcell + (states.trickle.value,)))
      continue

    if belowcellval == states.soil:
      setcellvalue(*(curcell + (states.trickle.value,)))
      visited.append(curcell)
      appendcelltopath(path, x_, y_+1)
      continue

    if belowcellval == states.trickle:
      setcellvalue(*(curcell + (states.trickle.value,)))
      continue
    
    if (belowcellval == states.clay or belowcellval == states.water):
      if cellisbounded(*curcell):
        fillrowwithwater(*curcell)
        appendcelltopath(path, *visited.pop())
      else:
        leftcellval, rightcellval = getcellvalue(x_-1, y_), getcellvalue(x_+1, y_)
        setcellvalue(*(curcell + (states.trickle.value,)))
        isstuck = True
        if leftcellval == states.soil:
          appendcelltopath(path, x_-1, y_)
          isstuck = False
        if rightcellval == states.soil:
          appendcelltopath(path, x_+1, y_)
          isstuck = False
        
        if isstuck and len(path) == 0 and len(visited) > 0:
          appendcelltopath(path, *visited.pop())

# Recursive implementation
def trickledownrecursive(x, y, comingfromleft=False, comingfromright=False):
  print(x, y)
  curcell = (x, y)
  cellval = getcellvalue(x, y)

  if cellval == states.clay or cellval == states.outofbounds:
    return

  trickles, y_ = 0, y

  setcellvalue(x, y_, states.trickle.value)
  while True:
    belowcellval = getcellvalue(x, y_+1)
    if belowcellval == states.soil or belowcellval == states.trickle:
      setcellvalue(x, y_, states.trickle.value)
      y_ += 1
      trickles += 1
    else:
      break

  tricked = trickles > 0
  if trickles > 0:
    comingfromleft = False
    comingfromright = False

  # get updated below cell value
  belowcellval = getcellvalue(x, y_+1)
  print('below', belowcellval, trickles, x, y_)

  if (belowcellval == states.clay or belowcellval == states.water):
    if not cellisbounded(x, y_):
      if not comingfromleft:
        trickledown(x-1, y_, False, True)
      if not comingfromright:
        trickledown(x+1, y_, True, False)

    if cellisbounded(x, y_):
      print('cell bounded')
      while cellisbounded(x, y_):
        print('filling with water', x, y_, trickles)
        fillrowwithwater(x, y_)
        if trickles > 0:
          trickles -= 1
          y_ -=  1
        else:
          break
      
      if tricked and not cellisbounded(x, y_):
        trickledown(x-1, y_, False, True)
        trickledown(x+1, y_, True, False)


def getwaterycells():
  global section
  return sum([sum([1 if c == states.trickle.value or c == states.water.value else 0 for c in r]) for r in section])

def getretainedcells():
  global section
  return sum([sum([1 if c == states.water.value else 0 for c in r]) for r in section])

section, minx, maxx, miny, maxy = getinput('input17.txt')

try:
  trickledown(500-minx, 0)
except:
  print('########### ERROR ###########', sys.exc_info()[0])
finally:
  print('~~~~~~~~~~~ FINALLY ~~~~~~~~~~~')
  printsection(section)
  print('Number of watery cells: {}'.format(getwaterycells()))
  print('Number of cells water retained: {}'.format(getretainedcells()))


# ########################
# # TESTS
# ########################
# section = []
# section.append(list('......+.......'))
# section.append(list('............#.'))
# section.append(list('.#..#.......#.'))
# section.append(list('.#..#..#......'))
# section.append(list('.#..#..#......'))
# section.append(list('.#.....#......'))
# section.append(list('.#.....#......'))
# section.append(list('.#######......'))
# section.append(list('..............'))
# section.append(list('..............'))
# section.append(list('....#.....#...'))
# section.append(list('....#.....#...'))
# section.append(list('....#.....#...'))
# section.append(list('....#######...'))

# printsection(section)

# assert cellisboundonleft(5,6) == True
# assert cellisboundonright(5,6) == True
# assert cellisbounded(5,6) == True