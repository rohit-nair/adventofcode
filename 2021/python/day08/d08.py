#! /usr/bin/env python3

from os import path
from typing import List, NamedTuple

class Segment(NamedTuple):
  pattern: str
  length: int

SEGEMENTS = {
  '0': Segment('', 6),
  '1': Segment('', 2),
  '2': Segment('', 5),
  '3': Segment('', 5),
  '4': Segment('', 4),
  '5': Segment('', 5),
  '6': Segment('', 6),
  '7': Segment('', 3),
  '8': Segment('', 7),
  '9': Segment('', 6),
}

UNIQUE_SEGMENTS_SIZE = [2, 4, 3, 7]

def process():
  input_val, output_val = get_input()

  uniq = get_unique_output_count(output_val)

  print(f'1, 4, 7, and 8 appear {uniq} times.')

  get_unique_outputs(output_val)

def get_unique_output_count(output_val:List):
  return sum([len(d) in UNIQUE_SEGMENTS_SIZE for l in output_val for d in l])

def get_unique_outputs(output_val:List):
  uniqs = [[d if len(d) in UNIQUE_SEGMENTS_SIZE else None for d in l] for l in output_val]
  print(uniqs)
  return uniqs


def get_input():
  with open(path.dirname(__file__) + '/testinput08.txt', 'r+') as f:
    input_val, output_val = tuple(zip(*[l.strip().split(' | ') for l in f.readlines()]))
    input_val, output_val = [i.split() for i in input_val], [o.split() for o in output_val]

    return input_val, output_val

process()