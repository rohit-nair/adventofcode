#!/usr/bin/env python

import heapq
from pprint import pprint

directions = { \
  '>': ((1, 0), '>'), \
  'v': ((0, 1), 'v'), \
  '<': ((-1, 0), '<'),\
  '^': ((0, -1), '^'),\
}

routes = None
# A queue of carts to determine the priority
cartpriority = []
# maintains the direction cart is heading and 
# the last direction it turned at an intersection
cartstate = {}

def getinput(file="testinput13.txt"):
  with open(file, 'r+') as f:
    return [list(l.rstrip('\n')) for l in f.readlines()]

def getcellvalue(inputs, x, y):
  if x < 0 or x >= len(inputs[0]) or y < 0 or y > len(inputs):
    return " "
  return inputs[y][x]

def cleanroutesandgetcarts(inputs):
  global routes
  routes = inputs.copy()
  cartcount = 0
  for y in range(len(routes)):
    for x in range(routes[0]:
      cellval = getcellvalue(routes, x, y)
      if cellval in directions.keys():
        cartid = "Cart - " + str(cartcount)
        heapq.heappush(cartpriority, (y, x, cartid))
        cartstate[cartid] = (cellval, None)
        routes[y][x] = 

def getnextstate(inputs, x, y, curstate):
  cell = getcellvalue(inputs, x, y)
  if cell in ('-', '|'):
    return (x - directions[curstate][0][0], y - directions[curstate][0][1]), directions[curstate][1]

  if cell == '\\':
    if curstate == '>':
      return (x+1, y), 'v'
    elif curstate == '<':
      return (x-1, y), '^'
    else:
      print('Unexpected transition. Cell {0}, current state {1}', cell, curstate )
  elif cell == '/':
    if curstate == '^':
      return (x, y-1), '>'
    elif curstate == 'v':
      return (x, y+1), '<'
    else:
      print('Unexpected transition. Cell {0}, current state {1}', cell, curstate )
  else:
      print('Unexpected transition. Cell {0}, current state {1}', cell, curstate )


def isintersection(x, y):
  pass

pprint(getinput())