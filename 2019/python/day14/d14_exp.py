#! /usr/bin/env python3
from collections import deque, defaultdict
from functools import reduce
import math
from pprint import pprint
from os import path

EOR = 'End of Reaction'

def calculate_fuel(index, reactions):
  q, chemicals, base_chemicals, visited = deque([(1, 'FUEL'), EOR]), defaultdict(int), defaultdict(int), set()
  
  while q:
    item = q.popleft()

    if item == EOR:

      for c in visited:
        (idx_qty, _), is_base_chemical = index[c]

        if is_base_chemical:
          base_chemicals[c] = chemicals[c]
          continue

        multiple = math.ceil(chemicals[c] / idx_qty)
        for react_qty, react_chem in reactions[(idx_qty, c)]:
          q.append((react_qty*multiple, react_chem))

        del chemicals[c]

      if len(q) > 0:
        q.append(EOR)

      visited = set()
      continue

    qty, chemical = item
    chemicals[chemical] += qty
    visited.add(chemical)


  ore = calculate_ore(index, reactions, base_chemicals)
  return ore



def calculate_fuel_stack(index, reactions, initial_state, leftovers):
  q, chemicals, base_chemicals = deque(initial_state), defaultdict(int), defaultdict(int)
  
  while q:
    qty, chemical = q.popleft()

    (idx_qty, _), is_base_chemical = index[chemical]

    if chemical in leftovers:
      whole_leftovers = int(leftovers[chemical])
      qty -= whole_leftovers
      leftovers[chemical] -= whole_leftovers

    if is_base_chemical:
      base_chemicals[chemical] += qty
      continue

    multiple = math.ceil(qty/idx_qty)
    leftovers[chemical] += multiple - qty/idx_qty

    for react_qty, react_chem in reactions[(idx_qty, chemical)]:
      q.appendleft((react_qty*multiple, react_chem))

  print(leftovers)
  ore = calculate_ore(index, reactions, base_chemicals)
  return ore

def calculate_fuel_leftovers(index, reactions):
  q, leftovers, ore, base_chemicals = deque([(1, 'FUEL')]), defaultdict(float), 0, defaultdict(int)

  while q:
    qty, chemical = q.popleft()

    if chemical == 'ORE':
      ore += qty
      continue

    if chemical in leftovers:
      whole_leftovers = int(leftovers[chemical])
      qty -= whole_leftovers
      leftovers[chemical] -= whole_leftovers

    (idx_qty, _), is_base_chemical = index[chemical]

    if is_base_chemical:
      base_chemicals[chemical] += qty
      continue

    multiple = math.ceil(qty/idx_qty)
    leftovers[chemical] += multiple - qty/idx_qty

    for react_qty, react_chem in reactions[(idx_qty, chemical)]:
      q.append((react_qty*multiple, react_chem))

  print(leftovers)
  ore = calculate_ore(index, reactions, base_chemicals)
  return ore

def calculate_ore(index, reactions, base_chemicals):
  ore_required = 0
  for chemical, qty in base_chemicals.items():
    (base_qty, _), __ = index[chemical]
    [(ore_qty, ___)] = reactions[(base_qty, _)]
    ore_required += math.ceil(qty/base_qty)*ore_qty
  return ore_required

def get_inputs(file='testinput14.txt'):
  reactions, index = {}, {}
  with open(path.join(path.dirname(__file__), file), 'r+') as f:
    for l in f.readlines():
      lhs, rhs = l.rstrip('\r').rstrip('\n').split('=>')
      qty, chemical = parse_chemical(rhs)
      derived_from = list(map(lambda x: parse_chemical(x), lhs.split(',')))

      gcd = reduce(math.gcd, [qty] + list(map(lambda x: x[0], derived_from)))
      gcd = 1

      reactions[(qty//gcd, chemical)] = list(map(lambda x: (x[0]//gcd, x[1]), derived_from))
      index[chemical] = ((qty//gcd, chemical), all(map(lambda x: x[1] == 'ORE', derived_from)))
  return index, reactions

def parse_chemical(chemical):
  qty, name = chemical.split()
  return int(qty), name

if __name__ == '__main__':
  i, r = get_inputs()
  leftovers = defaultdict(int)

  ore = calculate_fuel_stack(i, r, [(1, 'FUEL')], leftovers)
  print(ore)
  for k, v in leftovers.items():
    del leftovers[k]
    ore -= calculate_fuel_stack(i, r, [(v, k)], leftovers)
    print(ore)

  print(ore)
