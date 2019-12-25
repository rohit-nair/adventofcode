#! /usr/bin/env python3
from collections import deque
from os import path
from itertools import zip_longest;

ADD             = 1
MULTIPLY        = 2
INPUT           = 3
OUTPUT          = 4
JUMP_IF_TRUE    = 5
JUMP_IF_FALSE   = 6
LESS_THAN       = 7
EQUALS          = 8
UPDATE_REL_BASE = 9
HALT            = 99

POSITION  = 0
IMMEDIATE = 1
RELATIVE  = 2

READ    = 0
WRITE   = 1

OPERATIONS = {
  ADD: (READ, READ, WRITE),
  MULTIPLY: (READ, READ, WRITE),
  INPUT: (WRITE,),
  OUTPUT: (READ,),
  JUMP_IF_TRUE: (READ, READ),
  JUMP_IF_FALSE: (READ, READ),
  LESS_THAN: (READ, READ, WRITE),
  EQUALS: (READ, READ, WRITE),
  UPDATE_REL_BASE: (READ,),
  HALT: (),
}

class Processor:
  def __init__(self, program: list, inputs: list):
    self.program = program
    self.inputs = deque(inputs)
    self.idx = 0
    self.rel_base = 0
    self.len_program = len(program)
    self.outputs = deque([])
    self.stopped = False

  def process(self):
    while self.idx < self.len_program:
      operation = self.program[self.idx]
      operator = operation % 100
      modes = operation // 100

      arg_ops = OPERATIONS[operator]
      a, b, c = self._get_args(modes, arg_ops)

      if HALT == operator:
        self.stopped = True
        return
      elif ADD == operator:
        self.program[c] = a + b
      elif MULTIPLY == operator:
        self.program[c] = a * b
      elif INPUT == operator:
        while not self.inputs:
          yield
        self.program[a] = self.inputs.popleft()
      elif OUTPUT == operator:
        yield a
        self.outputs.append(a)
      elif JUMP_IF_TRUE == operator:
        if 0 != a:
          self.idx = b
          continue
      elif JUMP_IF_FALSE == operator:
        if 0 == a:
          self.idx = b
          continue
      elif LESS_THAN == operator:
        self.program[c] = 1 if a < b else 0 
      elif EQUALS == operator:
        self.program[c] = 1 if a == b else 0 
      elif UPDATE_REL_BASE == operator:
        self.rel_base += a
      else:
        self.is_running = False
        raise RuntimeError(f'Invalid opcode {operator}')

      self.idx += len(arg_ops) + 1

  def add_input(self, val):
    self.inputs.append(val)

  def _get_args(self, modes, arg_ops):
    args = [None] * 3

    for i, op in enumerate(arg_ops):
      mode = modes % 10
      modes //= 10
      val = self.program[self.idx + i + 1]

      if IMMEDIATE == mode:
        pass
      elif mode in (POSITION, RELATIVE):
        if RELATIVE == mode:
          val += self.rel_base

        if val >= self.len_program:
          self.program += [0] * self.len_program

        if READ == op:
          val = self.program[val]
      else:
        raise RuntimeError(f'Invalid mode {mode}')
      
      args[i] = val

    return args


def get_input(file='testinput05.txt'):
  with open(path.join(path.dirname(__file__), file), 'r+') as f:
    return [int(x) for x in f.readline().rstrip('\r').rstrip('\n').split(',')]

if __name__ == '__main__':
  act_input = get_input('input05.txt')
  p = Processor(act_input, (x for x in [5]))
  print(list(p.process()))
