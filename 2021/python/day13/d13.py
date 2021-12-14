#! /usr/bin/env python3

from collections import *
from os import path

def p1():
  data = get_input()
  max_x, max_y = max([x for x, _ in data])+1, max([y for _, y in data])+1
  
  paper = [['#' if (r, c) in data else '.' for r in range(max_x)] for c in range(max_y)]

  paper = fold_x(paper, 655)
  paper = fold_y(paper, 447)
  paper = fold_x(paper, 327)
  paper = fold_y(paper, 223)
  paper = fold_x(paper, 163)
  paper = fold_y(paper, 111)
  paper = fold_x(paper, 81)
  paper = fold_y(paper, 55)
  paper = fold_x(paper, 40)
  paper = fold_y(paper, 27)
  paper = fold_y(paper, 13)
  paper = fold_y(paper, 6)

  print_paper(paper)

  print(sum([paper[r][c] == '#' for r in range(len(paper)) for c in range(len(paper[0]))]))

def print_paper(paper):
  print('\n'.join([''.join(row) for row in paper]))


def fold_x(paper, x):
  for r in range(len(paper)):
    for c in range(x, len(paper[0])):
      if 2*x-c < 0 or paper[r][c] == '.':
        continue
      paper[r][2*x-c] = paper[r][c]
  return [row[:x] for row in paper]

def fold_y(paper, y):
  for r in range(y, len(paper)):
    for c in range(len(paper[0])):
      if 2*y-r < 0 or paper[r][c] == '.':
        continue
      paper[2*y-r][c] = paper[r][c]
  return paper[:y][:]

def get_input():
  with open(path.dirname(__file__) + '/input13.txt') as f:
    return {tuple(map(int, l.strip().split(','))) for l in f.readlines()}

p1()