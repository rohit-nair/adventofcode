#! /usr/bin/env python3

def compute(vals):
  i, l = 0, len(vals)
  if len(vals) < 4:
    return 0
  
  while i < l:
    if vals[i] == 99:
      return vals

    opcode, idx_x, idx_y, idx_res = vals[i:i+4]

    if opcode == 99:
      return vals
    elif opcode == 1:
      vals[idx_res] = vals[idx_x] + vals[idx_y]
    elif opcode == 2:
      vals[idx_res] = vals[idx_x] * vals[idx_y]
    else:
      raise RuntimeError(f'Invalid opcode {opcode}')

    i += 4

def get_input(file='testinput.txt'):
  with open(file, 'r+') as f:
    # print(f.readline().split(','))
    return [int(x) for x in f.readline().rstrip('\r').rstrip('\n').split(',')]

assert compute(get_input()) == [3500,9,10,70,2,3,11,0,99,30,40,50]

assert compute([1,0,0,0,99]) == [2,0,0,0,99], "Assertion failed testcase 1"
assert compute([2,3,0,3,99]) == [2,3,0,6,99], "Assertion failed testcase 2"
assert compute([2,4,4,5,99,0]) == [2,4,4,5,99,9801], "Assertion failed testcase 3"
assert compute([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99], "Assertion failed testcase 4"

act_input = get_input('input.txt')
act_input[1] = 12
act_input[2] = 2
print(compute(act_input)[0])