#!/usr/bin/env python

import re

INPUT=""
PATTERNS=set()
FIVEEMPTYPOTS="....."

def getinput(file="testinput12.txt"):
  global INPUT, PATTERNS

  first = True
  with open(file, 'r+') as f:
    for l in f.readlines():
      l = l.rstrip('\n').strip()
      if first:
        INPUT = l.replace("initial state: ", "") 
      elif len(l) > 0 and l.split(' => ')[1] == '#':
        PATTERNS.add(l.split(' => ')[0])
      first = False

def rungenerations(nbrofgens=20):
  i, zerothidx, initialstate, generation, sp = 0, 0, list(INPUT), list(INPUT), 0

  while i < nbrofgens:
    s = sum([i-zerothidx for i, v in enumerate(generation) if v == '#'])
    print('processing generation {0}, sum: {1}, delta: {2}\r'.format(i, s, s-sp))
    sp = s

    if initialstate.index('#') < 3:
      initialstate = list('...') + initialstate
      zerothidx += 3

    if list(reversed(initialstate)).index('#') < 3:
      initialstate = initialstate + list('...')

    generation = initialstate[:]

    # print(''.join(generation))
    # print(len(initialstate))
    for j in range(2, len(initialstate) - 2):
      # print(i, '####', j, ''.join(initialstate[j-2:j+3]), ''.join(initialstate[j-2:j+3]) in PATTERNS)
      generation[j] = '#' if ''.join(initialstate[j-2:j+3]) in PATTERNS else '.'
    
    i += 1
    initialstate = generation[:]
  return sum([i-zerothidx for i, v in enumerate(generation) if v == '#'])

getinput('testinput12.txt')
print(INPUT,PATTERNS)
# print(list(map(len, PATTERNS)))

# The delta (81) between generations starts repeating 
# after 100 gens. So use that to calculate sum after 
# 5b iterations!
sum100gen = rungenerations(100)
print(sum100gen + (50000000000-100)*81)