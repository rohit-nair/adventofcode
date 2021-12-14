#! /usr/bin/env python3

from collections import Counter, defaultdict, deque
from os import path

START, END, SEP = 'start', 'end', '-'
GRAPH = defaultdict(list)
PATHS = []

def p1():
  global GRAPH
  iput = get_input()
  for l, r in iput:
    GRAPH[l].append(r)
    if l != START and r != END:
      GRAPH[r].append(l)

  p = f'{START}{SEP}'
  dfs(START, p)

  print(f'{len(PATHS)} number of unique path.')


def dfs(node, p):
  global COUNT
  if node == END:
    PATHS.append(p)
    return

  for neigh in GRAPH[node]:
    if is_lowercased(neigh) and not can_pass_through(f'{p}{neigh}'):
      continue
    dfs(neigh, f'{p}{neigh}{SEP}')

def can_pass_through(p):
  occurences = Counter([n for n in p.split(SEP) if is_lowercased(n)])
  max_occ = sorted([cnt for _, cnt in occurences.items()])[-1]
  cnt_occ = Counter([cnt for _, cnt in occurences.items()])

  if max_occ < 2:
    return True
  elif max_occ == 2:
    return cnt_occ[max_occ] < 2
  else:
    return False

def is_lowercased(node):
  if len(node) == 0 or node == START or node == END:
    return False
  return all([ord(c) > 96 for c in list(node)])

def get_input():
  with open(path.dirname(__file__) + '/input12.txt') as f:
    return [l.strip().split('-') for l in f.readlines()]


assert False == is_lowercased('AB')
assert True == is_lowercased('ab')

assert can_pass_through('a-b-a') == True
assert can_pass_through('a-b-a-') == True
assert can_pass_through('a-b-c-d') == True
assert can_pass_through('a-b-a') == True
assert can_pass_through('a-b-a-c') == True
assert can_pass_through('a-b-a-a') == False
assert can_pass_through('a-b-a-b') == False

p1()