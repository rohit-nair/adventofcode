#! /usr/bin/env python3
from collections import namedtuple

class Result:
  def __init__(self, san, you):
    self.SAN = None
    self.YOU = None
    self.Ancestor = None

class Mass:
  def __init__(self, key):
    self.key = key
    self.children = []

  def add_child(self, child):
    self.children.append(child)

def create_graph(inputs):
  catalog, com = {}, None
  for inner, outer in inputs:
    if inner not in catalog:
      inner_mass = Mass(inner)
      catalog[inner] = inner_mass
    else:
      inner_mass = catalog[inner]

    if outer not in catalog:
      outer_mass = Mass(outer)
      catalog[outer] = outer_mass
    else:
      outer_mass = catalog[outer]

    if not com and inner == 'COM':
      com = inner_mass

    inner_mass.add_child(outer_mass)
  
  return com

def find_san_you(g, result, depth = 0):
  if result.Ancestor:
    return 0

  found = (result.YOU is not None) + (result.SAN is not None)
  initial_state = found
  g.depth = depth

  if g.key == 'YOU':
    result.YOU = depth
    found += 1
  elif g.key == 'SAN':
    result.SAN = depth
    found += 1
  
  if found == 2:
    return found - initial_state

  for c in g.children:
    found += find_san_you(c, result, depth+1)
  
  if result.Ancestor == None and initial_state == 0 and found == 2:
    result.Ancestor = g
  
  return found - initial_state

def get_input(file='testinput06.txt'):
  with open(file, 'r+') as f:
    return [l.rstrip('\r').rstrip('\n').split(')') for l in f.readlines()]

graph = create_graph(get_input())
res = Result(None, None)
find_san_you(graph, res)
print(res.SAN, res.YOU, res.Ancestor.depth)
assert res.SAN + res.YOU - 2*(res.Ancestor.depth + 1) == 4, 'assertion failed.'

g_test = create_graph(get_input('input06.txt'))
res_test = Result(None, None)
find_san_you(g_test, res_test)
print(res_test.SAN, res_test.YOU, res_test.Ancestor.depth)
print(f'Number of total hops between you and santa is: {res_test.SAN + res_test.YOU - 2*(res_test.Ancestor.depth + 1)}')
