#! /usr/bin/env python3

from os import path
import sys
from typing import Counter

def process():
  pos = get_input()
  historgram = get_histogram(pos)

  min_pos, cost = get_min_fuel_pos(historgram)

  print(f'Min cost is {cost} at {min_pos}.')

def get_min_fuel_pos(histogram: Counter):
  cost, min_pos = sys.maxsize, 0
  # for pos, nbr_crabs in histogram.most_common():
  for pos in range(max(list(histogram)) + 1):
    cost_pos = get_cost(histogram, pos)
    # print(f'Cost is {cost_pos} at {pos}.')
    if cost > cost_pos:
      cost = cost_pos
      min_pos = pos

  return min_pos, cost

def get_cost(histogram, pos_to_evaluate):
  return sum([sum(list(range(abs(p-pos_to_evaluate)+1)))*cnt for p, cnt in histogram.items()])

def get_histogram(pos):
  counter = Counter(pos)
  print(counter)
  return counter

def get_input():
  with open(path.dirname(__file__) + '/input07.txt', 'r+') as f:
    return list(map(int, f.readline().strip().split(',')))

process()