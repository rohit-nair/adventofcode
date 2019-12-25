#! /usr/bin/env python3

from itertools import cycle
import math
import numpy as np
from os import path

BASE_PATTERN = [0, 1, 0, -1]

def calculate_fft(inp, iterations=100):
  for i in range(iterations):
    inp = [abs(sum([a*b for a, b in zip([0]+inp, cycle(np.repeat(BASE_PATTERN, j+1)))]))%10 for j in range(len(inp))]
    print(inp)
  return ''.join([str(x) for x in inp[:8]])

if __name__ == '__main__':
  with open(path.join(path.dirname(__file__), 'input16.txt'), 'r+') as f:
    inp = [int(x) for x in '03036732577212944063491565474664'] #f.readline().strip()]
    print(f'First 8 digits are: {calculate_fft(inp*2)}')

    # #Part 2
    # offset = int(''.join(map(str, inp[:7])))
    # inp_len = len(inp)*10000
    # req_len = inp_len-offset
    # req_copies = math.ceil(req_len/len(inp))
    # print(inp_len, req_len, req_copies)
    # res = calculate_fft((inp*req_copies)[-req_len:])
    # print(res)