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

def find_magic_pair():
  act_input = get_input('input.txt')
  for noun in range(0, 100):
    for verb in range(0, 100):
      mod_input = act_input.copy()
      mod_input[1:3] = [noun, verb]
      output = compute(mod_input)[0]
      print(f'for noun: {noun}, verb: {verb} output: {output}')
      if output == 19690720:
        # print(f'##### Result: {100*noun + verb}')
        return 100*noun + verb

print(find_magic_pair())