#!/usr/bin/env python3

def read_inputs(p='testinput02.txt'):
  with open(p, 'r+') as f:
    return [sorted(map(int, l.rstrip('\n').split())) for l in f.readlines()]

def checksum(inputs):
  return sum([l[-1] - l[0] for l in inputs])

def checksum_division(inputs):
  s = 0
  for l in inputs:
    for i in range(len(l)):
      for j in range(i):
        s += l[i]/l[j] if l[i]%l[j] == 0 else 0

  return s

if __name__ == '__main__':
  print(read_inputs())
  assert [
    [1, 5, 5, 9], 
    [3, 5, 7], 
    [2, 4, 6, 8]] == read_inputs(), 'Woopsies!'

  assert 18 == checksum(read_inputs()), "Woopsies! checksum doesn't work."

  print('Test Result: {0}'.format(checksum(read_inputs())))

  print('Result: {0}'.format(checksum(read_inputs('input02.txt'))))

  assert 9 == checksum_division(read_inputs('testinput02_2.txt')), "Woopsies! checksum doesn't work."

  print('Test Result: {0}'.format(checksum_division(read_inputs('testinput02_2.txt'))))

  print('Result: {0}'.format(checksum_division(read_inputs('input02_2.txt'))))

