#! /usr/bin/env python

# Fuel = mass//3 - 2
def find_fuel(mass):
  res = 0
  while mass > 0:
    mass = mass//3 - 2
    res += mass if mass > 0 else 0
  return res

assert find_fuel(12) == 2, "Assertion failed 1."
#assert find_fuel(14) == 2, "Assertion failed 2."
assert find_fuel(1969) == 966, "Assertion failed 3."
assert find_fuel(100756) == 50346, "Assertion failed 4."


def getinput():
  with open('input01.txt', 'r+') as f:
    return map(int, map(lambda x: x.rstrip('\n'), f.readlines()))

print(sum(map(find_fuel, getinput())))