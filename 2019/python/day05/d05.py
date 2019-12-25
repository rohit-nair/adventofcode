#! /usr/bin/env python3
from itertools import zip_longest;

def compute(vals, inputs, outputs):
  i, increment, rel_base, l = 0, 0, 0, len(vals)
  for o in outputs:
    yield o

  while i < l:
    poi = str(vals[i])
    pmodes, opcode = list(reversed(list(poi[:-2]))), int(poi[-2:])

    if opcode == 99:
      # halt
      return result
    elif opcode == 1:
      # add
      idx_x, idx_y, idx_res = zip_longest(pmodes, vals[i+1:i+4], fillvalue='0')
      vals[idx_res[1]] = get_value(vals, *idx_x) + get_value(vals, *idx_y)
      increment = 4
    elif opcode == 2:
      # multiply
      idx_x, idx_y, idx_res = zip_longest(pmodes, vals[i+1:i+4], fillvalue='0')
      vals[idx_res[1]] = get_value(vals, *idx_x) * get_value(vals, *idx_y)
      increment = 4
    elif opcode == 3:
      # input
      vals[vals[i+1]] = next(inputs)
      increment = 2
    elif opcode == 4:
      # output
      increment = 2
      pmode = pmodes[-1] if len(pmodes) > 0 else '0'
      result = get_value(vals, pmode, vals[i+1])
      yield result
    elif opcode == 5:
      # jump if true
      idx_x, idx_res = zip_longest(pmodes, vals[i+1:i+3], fillvalue='0')
      val = get_value(vals, *idx_x)
      if not val == 0:
        i = get_value(vals, *idx_res)
        continue
      else:
        increment = 3
    elif opcode == 6:
      # jump if false
      idx_x, idx_res = zip_longest(pmodes, vals[i+1:i+3], fillvalue='0')
      val = get_value(vals, *idx_x)
      if val == 0:
        i = get_value(vals, *idx_res)
        continue
      else:
        increment = 3
    elif opcode == 7:
      # less than
      idx_x, idx_y, idx_res = zip_longest(pmodes, vals[i+1:i+4], fillvalue='0')
      val_x, val_y = map(lambda p: get_value(vals, *p), [idx_x, idx_y])
      if val_x < val_y:
        vals[idx_res[1]] = 1
      else:
        vals[idx_res[1]] = 0
      increment = 4
    elif opcode == 8:
      # equals
      idx_x, idx_y, idx_res = zip_longest(pmodes, vals[i+1:i+4], fillvalue='0')
      val_x, val_y = map(lambda p: get_value(vals, *p), [idx_x, idx_y])
      if val_x == val_y:
        vals[idx_res[1]] = 1
      else:
        vals[idx_res[1]] = 0
      increment = 4
    elif opcode == 9:
      # update relative base
      idx_x = zip_longest(pmodes, vals[i+1:i+2], fillvalue='0')
      val_x = get_value(vals, *idx_x)
      rel_base += val_x
      increment = 2
    else:
      raise RuntimeError(f'Invalid opcode {opcode}')

    i += increment

def get_value(vals, mode, val):
  res = vals[val] if mode == '0' else val
  return res

def get_input(file='testinput.txt'):
  with open(file, 'r+') as f:
    # print(f.readline().split(','))
    return [int(x) for x in f.readline().rstrip('\r').rstrip('\n').split(',')]

# print(compute([1101,100,-1,4,0]))
# assert compute([1101,100,-1,4,0]) == 1101, "Assertion failed."
# print(compute([1002,4,3,4,33], 1))
# assert compute([1002,4,3,4,33], 1) == 1002, "Assertion #2 failed."

if __name__ == '__main__':
  act_input = get_input('2019/python/day05/input05.txt')
  print(list(compute(act_input, (x for x in [5]), [])))
