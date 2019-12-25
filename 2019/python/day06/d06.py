#! /usr/bin/env python3

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

def find_orbits(g, depth = 0):
  total_orbits, g.orbits = depth, depth
  for c in g.children:
    total_orbits += find_orbits(c, depth+1)
  return total_orbits

def get_input(file='testinput06.txt'):
  with open(file, 'r+') as f:
    return [l.rstrip('\r').rstrip('\n').split(')') for l in f.readlines()]

graph = create_graph(get_input())
assert find_orbits(graph) == 42, 'assertion failed.'

g_test = create_graph(get_input('input06.txt'))
print(f'Number of total orbits in this system is {find_orbits(g_test)}')
