#! /usr/bin/env python

import numpy as np

# Find the fuel cell's rack ID, which is its X coordinate plus 10.
# Begin with a power level of the rack ID times the Y coordinate.
# Increase the power level by the value of the grid serial number (your puzzle input).
# Set the power level to itself multiplied by the rack ID.
# Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
# Subtract 5 from the power level.
def calculatepower(x, y, serialnbr = 4455):
  rackid = x + 10
  return (((rackid*y+serialnbr)*rackid//100)%10) - 5


def getgrid(serialnbr = 4455):
  return np.array([[calculatepower(x, y, serialnbr) for x in range(1, 301)] for y in range(1, 301)])

def calculatepowercord(serialnbr = 4455):
  grid = getgrid(serialnbr)
  mval, cel = float('-inf'), tuple()
  for y in range(1, 301-3):
    for x in range(1, 301-3):
      s = sum(sum(grid[y-1:y-1+3, x-1:x-1+3]))
      if s > mval:
        mval = s
        cel = (x,y)
  return cel, mval


def calculatepowercordanysize(serialnbr = 4455):
  grid = getgrid(serialnbr)
  sz, mval, cel = 2, float('-inf'), tuple()
  
  while sz < 300:
    print(sz, end='\r')
    for y in range(1, 301-sz):
      for x in range(1, 301-sz):
        s = sum(sum(grid[y-1:y-1+sz, x-1:x-1+sz]))
        if s > mval:
          mval = s
          cel = ((x,y), sz)
    sz += 1
  return cel, mval



assert calculatepower(3,5,8) == 4, "Test case 1 failed."
assert calculatepower(122,79,57) == -5, "Test case 2 failed."
assert calculatepower(217,196,39) == 0, "Test case 3 failed."
assert calculatepower(101,153,71) == 4, "Test case 4 failed."

assert calculatepowercord(18) == ((33, 45), 29), "Test case 5 failed."

# print(calculatepowercord())
print(calculatepowercordanysize())