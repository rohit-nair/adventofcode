#!/usr/bin/env python3

import json
from enum import Enum
from pprint import pprint
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
    self.hierarchy = []
    if self._findendofdirection(0) != -1:
      self.process_frag()

  def __str__(self):
    # return "frag: {0},\n hierarchy: {1},\n children: {2}\n____________".format(
    #   self.frag,
    #   '\n'.join(map(str, self.hierarchy)),
    #   '\n'.join(map(str, self.children)))
    return json.dumps(self.__dict__)

  def process_frag(self):
    print(self.frag)
    i, curNode, foundBranch = 0, None, False
    while i < len(self.frag):
      curchar = self.frag[i]

      if curchar == '(':
        # Branch! Go deeper
        endofbranch = self._getmatchingendparen(i)
        n = Node(self.frag[i+1:endofbranch])
        if curNode == None:
          curNode = n
        else:
          curNode.hierarchy.append(n)

        i = endofbranch + 1
      elif curchar == ')':
        # Done with the branches.
        # Also add a node here where all the previous branches 
        raise Exception('Unexpected end paren at {}.'.format(i)) 
      elif curchar == '|':
        # Add another option to current level
        self.children.append(Node('') if curNode == None else curNode)
        # reset state
        curNode = None
        i += 1
        foundBranch = True
      else:
        endofdirection = self._findendofdirection(i)
        if endofdirection == -1:
          n = Node(self.frag[i:])
          i = len(self.frag)
        else:
          n = Node(self.frag[i:endofdirection])
          i = endofdirection

        if curNode == None:
          curNode = n
        else:
          curNode.hierarchy.append(n)

    curNode = Node('') if curNode == None else curNode
    if foundBranch:
      self.children.append(curNode)
    else:
      self.hierarchy.append(curNode)

  def unravel(self):
    '''
    rtype: list of strings
    '''
    pass

  def _findendofdirection(self, start):
    idxparen = self.frag.find('(', start)
    idxpipe = self.frag.find('|', start)
    idxendparen = self.frag.find(')', start)

    if idxparen == idxpipe == idxendparen == -1:
      return -1

    return min(float('inf') if idxparen == -1 else idxparen,
      float('inf') if idxendparen == -1 else idxendparen,
      float('inf') if idxpipe == -1 else idxpipe)

  def _getmatchingendparen(self, startparen):
    cntparen = 0
    for i in range(startparen, len(self.frag)):
      if self.frag[i] == '(':
        cntparen += 1
      elif self.frag[i] == ')':
        cntparen -= 1
        if cntparen == 0:
          return i
    return -1

  def _getmatchingstartparen(self, endparen):
    cntparen = 0
    for i in range(endparen, -1, -1):
      if self.frag[i] == ')':
        cntparen += 1
      elif self.frag[i] == '(':
        cntparen -= 1
        if cntparen == 0:
          return i
    return -1

def getinput():
  with open('input20.txt', 'r+') as f:
    return f.readline().rstrip('\n')


if __name__ == "__main__":
  # direction = getinput()

  #################
  # TEST
  #################
  # directions = '^ENWWW((W|)NEEE|SSE(EE|N))$'
  directions = getinput()
  n = Node(directions[1:-1])
  # assert n._getmatchingendparen(5) == 20, "Woops, end parent index incorrect"
  # assert n._getmatchingendparen(14) == 19, "Woops, end parent index incorrect"
  # assert n._getmatchingstartparen(20) == 5, "Woops, start parent index incorrect"
  # assert n._getmatchingstartparen(19) == 14, "Woops, start parent index incorrect"
  print(json.dumps(n, indent=2, sort_keys=True, default=lambda x: x.__dict__))
