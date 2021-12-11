#! /usr/bin/env python3

from collections import Counter, defaultdict
import math
from os import path
from dataclasses import dataclass
from typing import List, TypedDict

DEFAULT_TIMER = 6
NEW_FISH_TIMER = 8

@dataclass(repr=True, order=True)
class Fish():
  timer:int
  gen: int  # Generation

class School(TypedDict):
  gen: int
  fishes: List[Fish]

def process():
  school = get_input()
  
  days, fishes_day_before = 80, None
  for d in range(days):
    process_day(school)
    size_school = sum([len(f) for f in school.values()])

    # delta, delta_day_before = size_school - (fishes_day_before or 0), 0
    # ratio, ratio_day_before = size_school/(fishes_day_before or 1), 1
    # print(f'There are {size_school} lanternfish after {d} days. Log: {math.log(size_school or 1, 7)} {(delta-delta_day_before)/(delta_day_before or 1)} increase. Ratio: {(ratio-ratio_day_before)/(ratio_day_before or 1)}.')
    # fishes_day_before = size_school
    # delta_day_before = delta

  print(f'There are {size_school} lanternfish after {days} days.')

def process_day(school):
  born = []
  for gen in school.values():
    for fish in gen:
      newborn = get_updated_timer(fish)
      if newborn:
        born.append(fish.gen + 1)
  
  for gen in born:
    school.setdefault(gen, []).append(Fish(NEW_FISH_TIMER, gen))

def get_updated_timer(fish_gen: Fish):
  newborn = False
  if fish_gen.timer == 0:
    fish_gen.timer = DEFAULT_TIMER
    newborn = True
  else:
    fish_gen.timer -= 1

  return newborn

def get_input():
  with open(path.dirname(__file__) + '/input06.txt', 'r+') as f:
    line = f.readline().strip().split(',')
    # TODO: Generation logic is incorrect. Generations are the timer value.
    return {0: list(map(lambda x: Fish(int(x), 0), line))}


process()


def p2():
  school = Counter(list(map(int, open(path.dirname(__file__) + '/input06.txt').readline().strip().split(','))))
  
  DAYS = 256
  for d in range(DAYS):
    new_school = defaultdict(int)
    for gen, cnt in school.items():
      if gen == 0:
        new_school[DEFAULT_TIMER] += cnt
        new_school[NEW_FISH_TIMER] += cnt
      else:
        new_school[gen-1] += cnt
    school = new_school
    # print(f'Total lanternfish after {d} is {sum(school.values())}.')

  print(f'Total lanternfish after {DAYS} is {sum(school.values())}.')


process()

p2()