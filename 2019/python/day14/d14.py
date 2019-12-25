#! /usr/bin/env python3

from collections import defaultdict
import math
from os import path

def calculate_ore(qty, chemical):
  stack, chemicals = [chemical], defaultdict(int)
  chemicals[chemical] = -qty

  while stack:
    chemical = stack.pop()

    required = -chemicals[chemical]
    react_out, react_inputs = reactions[chemical]
    repetition = math.ceil(required/react_out)
    chemicals[chemical] += react_out*repetition

    for react_qty, react_chem in react_inputs:
      chemicals[react_chem] -= react_qty*repetition
      if react_chem != 'ORE' and chemicals[react_chem] < 0:
        stack.append(react_chem)

  return -chemicals['ORE']

def parse_chemical(chemical):
  qty, name = chemical.split()
  return int(qty), name

with open(path.join(path.dirname(__file__), 'input14.txt'), 'r+') as f:
  reactions = {}
  for l in f.readlines():
    lhs, rhs = l.strip().split('=>')
    qty, chemical = parse_chemical(rhs)
    derived_from = [parse_chemical(x) for x in lhs.split(',')]
    reactions[chemical] = (qty, derived_from)

  ore = calculate_ore(1, 'FUEL')
  print(f"Ore required: {ore}")

  lower_bound_fuel = 10**12 // ore
  upper_bound_fuel = 2*lower_bound_fuel

  while lower_bound_fuel < upper_bound_fuel:
    fuel = (upper_bound_fuel + lower_bound_fuel + 1) // 2
    if calculate_ore(fuel, 'FUEL') > 10**12:
      upper_bound_fuel = fuel-1
    else:
      lower_bound_fuel = fuel
  
  print(f'Max fuel: {fuel}')
