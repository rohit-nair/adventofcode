#! /usr/bin/env python3

from os import path

def execute():
  with open(path.join(path.dirname(__file__), 'input01.txt'), 'r+') as f:
    counter, prev_input = 0, None
    for l in f.readlines():
      val = int(l.strip())

      if prev_input is None:
        prev_input = val
        continue
      
      if val > prev_input:
        counter += 1
      
      prev_input = val

  print(f'{counter} measurements were larger than previous measurement.')

def execute_part_2():
  with open(path.join(path.dirname(__file__), 'input01.txt'), 'r+') as f:
    counter, sliding_window = 0, []
    for l in f.readlines():
      val = int(l.strip())

      sliding_window.append(val)

      if sum(sliding_window[:3]) < sum(sliding_window[1:]):
        counter += 1
      
      if len(sliding_window) > 3:
        del sliding_window[0]
  
  print(f'{counter} measurements were larger than previous measurement.')
      

if __name__ == '__main__':
  execute()
  execute_part_2()