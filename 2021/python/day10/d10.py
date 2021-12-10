#! /usr/bin/env python3

from collections import deque
from os import path

STARTING_CLOSING_BRACKETS = {
  '(': ')', 
  '[': ']', 
  '{': '}', 
  '<': '>', 
}

BRACKET_SCORE = {
  ')': 3, 
  ']': 57, 
  '}': 1197, 
  '>': 25137, 
}

CLOSING_BRACKET_SCORE = {
  '(': 1, 
  '[': 2, 
  '{': 3, 
  '<': 4, 
}

def process():
  code = get_input()
  score, incomplete_score = get_compiler_score(code)

  print(f'Total syntax error score is {score}.')
  print(f'Incomplete syntax error score is {incomplete_score}.')

def get_compiler_score(code):
  compiler_score, incomplete_scores = 0, []
  for c in code:
    is_corrupt, is_incomplete, score = is_corrupt_code(c)
    if is_corrupt:
      compiler_score += score
    elif is_incomplete:
      incomplete_scores.append(score)

  print(f'Incomplete scores: {incomplete_scores}')
  compiler_incomplete_score = sorted(incomplete_scores)[len(incomplete_scores)//2]

  return compiler_score, compiler_incomplete_score

def is_corrupt_code(line):
  idx, stack, length = 0, deque([]), len(line)
  while idx < length:
    c = line[idx]
    if c in STARTING_CLOSING_BRACKETS:
      stack.append(c)
    else:
      last_starting_bracket = stack[-1]
      if STARTING_CLOSING_BRACKETS[last_starting_bracket] != c:
        print(f'Corrupted line. Expected {last_starting_bracket} got {c}.')
        return True, False, BRACKET_SCORE[c]
      else:
        stack.pop()
    idx += 1

  incomplete_score = 0
  if len(stack) > 0:
    print(f'Incomplete line. Missing {"".join(stack)}.')
    while len(stack) > 0:
      last_starting_bracket = stack.pop()
      score = CLOSING_BRACKET_SCORE[last_starting_bracket]
      incomplete_score = ((incomplete_score*5) + score)

    return False, True, incomplete_score

  return False, len(stack) > 0, incomplete_score



def get_input():
  with open(path.dirname(__file__) + '/input10.txt', 'r+') as f:
    return [l.strip() for l in f.readlines()]

process()