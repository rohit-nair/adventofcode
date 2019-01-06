#!/usr/bin/env python

import ast
from collections import defaultdict
from pprint import pprint

__all__ = [
  'addi',
  'addr',
  'bani',
  'banr',
  'bori',
  'borr',
  'eqir',
  'eqri',
  'eqrr',
  'gtir',
  'gtri',
  'gtrr',
  'muli',
  'mulr',
  'seti',
  'setr',
  'executeop']

inputs = []
testinputs = []
trackopcodes = defaultdict(dict)

def operate(i, *args):
  registers, operation, result = args[0]
  opcode, operandA, operandB, operandC = operation
  cntsuccess = 0
  
  res = addr(registers[:], operandA, operandB, operandC) == result
  if 'addr' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['addr'] += res
  else:
    trackopcodes[opcode]['addr'] = 1
  cntsuccess += res
  
  res = addi(registers[:], operandA, operandB, operandC) == result
  if 'addi' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['addi'] += res
  else:
    trackopcodes[opcode]['addi'] = 1
  cntsuccess += res
  
  res = mulr(registers[:], operandA, operandB, operandC) == result
  if 'mulr' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['mulr'] += res
  else:
    trackopcodes[opcode]['mulr'] = 1
  cntsuccess += res
  
  res = muli(registers[:], operandA, operandB, operandC) == result
  if 'muli' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['muli'] += res
  else:
    trackopcodes[opcode]['muli'] = 1
  cntsuccess += res
  
  res = banr(registers[:], operandA, operandB, operandC) == result
  if 'banr' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['banr'] += res
  else:
    trackopcodes[opcode]['banr'] = 1
  cntsuccess += res
  
  res = bani(registers[:], operandA, operandB, operandC) == result
  if 'bani' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['bani'] += res
  else:
    trackopcodes[opcode]['bani'] = 1
  cntsuccess += res
  
  res = borr(registers[:], operandA, operandB, operandC) == result
  if 'borr' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['borr'] += res
  else:
    trackopcodes[opcode]['borr'] = 1
  cntsuccess += res
  
  res = bori(registers[:], operandA, operandB, operandC) == result
  if 'bori' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['bori'] += res
  else:
    trackopcodes[opcode]['bori'] = 1
  cntsuccess += res
  
  res = setr(registers[:], operandA, operandB, operandC) == result
  if 'setr' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['setr'] += res
  else:
    trackopcodes[opcode]['setr'] = 1
  cntsuccess += res
  
  res = seti(registers[:], operandA, operandB, operandC) == result
  if 'seti' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['seti'] += res
  else:
    trackopcodes[opcode]['seti'] = 1
  cntsuccess += res
  
  res = gtir(registers[:], operandA, operandB, operandC) == result
  if 'gtir' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['gtir'] += res
  else:
    trackopcodes[opcode]['gtir'] = 1
  cntsuccess += res
  
  res = gtri(registers[:], operandA, operandB, operandC) == result
  if 'gtri' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['gtri'] += res
  else:
    trackopcodes[opcode]['gtri'] = 1
  cntsuccess += res
  
  res = gtrr(registers[:], operandA, operandB, operandC) == result
  if 'gtrr' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['gtrr'] += res
  else:
    trackopcodes[opcode]['gtrr'] = 1
  cntsuccess += res
  
  res = eqir(registers[:], operandA, operandB, operandC) == result
  if 'eqir' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['eqir'] += res
  else:
    trackopcodes[opcode]['eqir'] = 1
  cntsuccess += res
  
  res = eqri(registers[:], operandA, operandB, operandC) == result
  if 'eqri' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['eqri'] += res
  else:
    trackopcodes[opcode]['eqri'] = 1
  cntsuccess += res
  
  res = eqrr(registers[:], operandA, operandB, operandC) == result
  if 'eqrr' in trackopcodes[opcode].keys():
    trackopcodes[opcode]['eqrr'] += res
  else:
    trackopcodes[opcode]['eqrr'] = 1
  cntsuccess += res
  
  return cntsuccess

def addr(regs, regA, regB, regC):
  regs[regC] = regs[regA] + regs[regB]
  return regs

def addi(regs, regA, valB, regC):
  regs[regC] = regs[regA] + valB
  return regs

def mulr(regs, regA, regB, regC):
  regs[regC] = regs[regA] * regs[regB]
  return regs

def muli(regs, regA, valB, regC):
  regs[regC] = regs[regA] * valB
  return regs

def banr(regs, regA, regB, regC):
  regs[regC] = regs[regA] & regs[regB]
  return regs

def bani(regs, regA, valB, regC):
  regs[regC] = regs[regA] & valB
  return regs

def borr(regs, regA, regB, regC):
  regs[regC] = regs[regA] | regs[regB]
  return regs

def bori(regs, regA, valB, regC):
  regs[regC] = regs[regA] | valB
  return regs

def setr(regs, regA, valB, regC):
  regs[regC] = regs[regA]
  return regs

def seti(regs, valA, valB, regC):
  regs[regC] = valA
  return regs

def gtir(regs, valA, regB, regC):
  regs[regC] = 1 if valA > regs[regB] else 0
  return regs

def gtri(regs, regA, valB, regC):
  regs[regC] = 1 if regs[regA] > valB else 0
  return regs

def gtrr(regs, regA, regB, regC):
  regs[regC] = 1 if regs[regA] > regs[regB] else 0
  return regs

def eqir(regs, valA, regB, regC):
  regs[regC] = 1 if valA == regs[regB] else 0
  return regs

def eqri(regs, regA, valB, regC):
  regs[regC] = 1 if regs[regA] == valB else 0
  return regs

def eqrr(regs, regA, regB, regC):
  regs[regC] = 1 if regs[regA] == regs[regB] else 0
  return regs

def getinput(file="input16.txt"):
  testprog, cur, emptytracker = False, [], []
  with open(file, 'r+') as f:
    for l in f.readlines():
      l = l.rstrip('\n')

      if len(l) == 0:
        emptytracker.append(True)
      elif len(emptytracker):
        emptytracker.pop()

      if len(emptytracker) == 3 and all(emptytracker):
        testprog = True

      if testprog and not len(l) == 0:
        testinputs.append(map(int, l.split()))
        continue
       
      if len(l) == 0:
        continue
      
      if l.find("Before: ") != -1:
        if len(cur) != 0:
          inputs.append(cur)
        cur = [ast.literal_eval(l.replace("Before: ", "").strip())]
      elif l.find("After: ") != -1:
        cur.append(ast.literal_eval(l.replace("After: ", "").strip()))
      else:
        cur.append(map(int, l.split()))

_map_opname_to_func = {
  'addi': addi, 
  'addr': addr, 
  'bani': bani, 
  'banr': banr, 
  'bori': bori, 
  'borr': borr, 
  'eqir': eqir, 
  'eqri': eqri, 
  'eqrr': eqrr, 
  'gtir': gtir, 
  'gtri': gtri, 
  'gtrr': gtrr, 
  'muli': muli, 
  'mulr': mulr, 
  'seti': seti,
  'setr': setr
}

def executeop(op, registers, operandA, operandB, operandC):
  _map_opname_to_func[op](registers, operandA, operandB, operandC)

if __name__ == '__main__':
  ###################################
  # PART 1
  ###################################
  getinput()

  res1 = 0
  for i, v in enumerate(inputs):
    res1 += operate(i, v) > 2
  print('{} samples behave like three or more opcodes.'.format(res1))





  ###################################
  # PART 2
  ###################################

  # dict to handle operation sets
  codeopmapping = {}
  all_ops = set()

  for k, v in trackopcodes.items():
    # print(k, v)
    max_val = max(v.values())
    poss_ops = set([key for key, value in v.items() if value == max_val])

    all_ops |= poss_ops
    codeopmapping[k] = poss_ops

  # print(codeopmapping)


  ops = {}
  while len(all_ops) > 0:
    found_ops = set()
    for k, v in codeopmapping.items():
      if len(v) == 1:
        (found_op,) = v
        ops[k] = found_op
        found_ops.add(found_op)

    all_ops -= found_ops

    for k in codeopmapping.keys():
      codeopmapping[k] -= found_ops
      if len(codeopmapping[k]) == 0:
        del codeopmapping[k]

  pprint(sorted([(k, v) for k, v in ops.items()]))

  # Compute final stae of register
  registers = [0, 0, 0, 0]
  for v in testinputs:
    opcode, operandA, operandB, operandC = v
    _map_opname_to_func[ops[opcode]](registers, operandA, operandB, operandC)


  print('Final state of registers is {}'.format(registers))









