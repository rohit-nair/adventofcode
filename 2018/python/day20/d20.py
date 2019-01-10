#!/usr/bin/env python3

from enum import Enum

class Elements(Enum):
  Room = '.'
  Wall = '#'
  WEDoor = '|'
  NSDoor = '-'
  Start = 'X'

class Node():
  def __init__(self, frag):
    self.frag = frag
    self.children = []

def getinput():
  with open('input20.txt', 'r+') as f:
    return f.readline().rstrip('\n')

def getdirections(directions):
  pass

def processinput(directions, start, end):
  curfrag, curlevel, levels = "", [], []

  for i in range(start, end):
    pass

def getmatchingendparen(directions, startparen):
  cntparen = 0
  for i in range(startparen, len(directions)):
    if directions[i] == '(':
      cntparen += 1
    elif directions[i] == ')':
      cntparen -= 1
      if cntparen == 0:
        return i
  return -1




if __name__ == "__main__":
  # direction = getinput()

  #################
  # TEST
  #################
  directions = '^ENWWW(NEEE|SSE(EE|N))$'
  assert getmatchingendparen(directions, 6) == 21, "Woops, end parent index incorrect"

  assert getmatchingendparen(directions, 15) == 20, "Woops, end parent index incorrect"