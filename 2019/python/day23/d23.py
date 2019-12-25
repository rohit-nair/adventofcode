#! /usr/env/bin python3

from ..day05.intCode import Processor
from collections import deque
from os import path

def start_networking():
  ps = [Processor(code.copy(), [_]) for _ in range(50)]
  gens = [p.process() for p in ps]
  inputs = [deque([]) for _ in ps]
  prev_nat_x, prev_nat_y, nat_x, nat_y = None, None, None, None
  first_nat_triggered = False
  while True:
    for idx, p in enumerate(ps):
      if inputs[idx]:
        x, y = inputs[idx].popleft()
        p.add_input(x)
        p.add_input(y)
      else:
        p.add_input(-1)
      val = next(gens[idx]), next(gens[idx]), next(gens[idx])
      if not val[0]:
        continue
      next_idx, x, y = val
      if next_idx == 255:
        nat_x, nat_y = x, y
        if not first_nat_triggered:
          yield nat_y
          first_nat_triggered = True
      if val[0] < 0 or val[0] > 49:
        continue
      inputs[next_idx].append((x,y))
    
    if sum(map(len, inputs)) == 0:
      inputs[0].append((nat_x, nat_y))
      if prev_nat_y == nat_y:
        yield nat_y
        return
      prev_nat_x, prev_nat_y = nat_x, nat_y


if __name__ == '__main__':
  with open(path.join(path.dirname(__file__), 'input23.txt'), 'r+') as f:
    code = [int(x) for x in f.readline().strip().split(',')]
    res = start_networking()
    print(f'First NAT Y: {next(res)}, Repeating NAT Y: {next(res)}')
    