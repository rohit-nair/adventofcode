#!/usr/bin/env python
import re, string

def getinput(file='testinput.txt'):
  with open(file, 'r+') as f:
    return f.readlines()[0].rstrip('\n')

def processinput(input):
  i, j, mlen, linput, removed = 0, 1, len(input), list(input), '#'

  while i+1 < len(linput):
    l, r = linput[i], linput[i+1]
    
    if l.lower() == r.lower() and l != r:
      # remove these characters
      del linput[i], linput[i]

      if i > 0:
        i -= 1
      continue
    
    i += 1

  # return sum([1 if x != removed else 0 for x in linput])
  return ''.join(linput)

def findoptimalreduction(input):
  mc, mlen = None, float('inf')
  for c in string.ascii_lowercase:
    rex = re.compile(c, re.IGNORECASE)
    opts = processinput(rex.sub('', input))
    optlen = len(opts)
    if optlen < mlen:
      mc, mlen = c, optlen
  return mlen


print(findoptimalreduction(getinput('input.txt')))