#!/usr/bin/env python3
import os
from pprint import pprint
from python.day16.d16 import executeop

def getinput(file='testinput19.txt'):
  this_file = os.path.abspath(__file__)
  this_dir = os.path.dirname(this_file)
  with open(os.path.join(this_dir, file), 'r+') as f:
    inputs = [l.rstrip('\n').split() for l in f.readlines()]
  for i in range(len(inputs)):
    inputs[i][1:len(inputs[i])] = map(int, inputs[i][1:len(inputs[i])])

  return inputs

def processinputs(inputs, ip, registers):
  i, ipval = 0, 0
  while i < len(inputs):
    op, operandA, operandB, operandC = inputs[i]
    registers[ip] = ipval
    executeop(op, registers, operandA, operandB, operandC)
    ipval = registers[ip] + 1
    i = ipval
  return registers[0]


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

if __name__ == '__main__':
  statements = getinput('input19.txt')
  # pprint(locals())
  res = processinputs(statements[1:], statements[0][1], [0,0,0,0,0,0])
  print('Value of register 0 after processing is {}'.format(res))
