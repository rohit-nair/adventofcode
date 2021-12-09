#! /usr/bin/env python3

from collections import Counter
from os import path

def execute():
  diagnostics = read_input()

  diagnostics_counter = get_counter(diagnostics)

  gamma_rate, epsilon_rate = get_gamma_and_epsilon(diagnostics_counter)

  print(f'From the diagnostics report, gamma rate is {gamma_rate} and '
  f'the epsilon rate is {epsilon_rate}. Power consumption is {gamma_rate*epsilon_rate}.')

def get_counter(diagnostics):
    diagnostics_counter = list(map(lambda x: Counter(x), zip(*diagnostics)))
    return diagnostics_counter

def get_gamma_and_epsilon(diagnostics_counter):
    b_gamma_rate, b_epsilon_rate = '', ''
    for c in diagnostics_counter:
      mc = c.most_common(1)[0][0]
      b_gamma_rate += mc
      b_epsilon_rate += str(1-int(mc))

    gamma_rate, epsilon_rate = int(b_gamma_rate, 2), int(b_epsilon_rate, 2)
    return gamma_rate,epsilon_rate

def read_input():
    diagnostics = []
    with open(path.join(path.dirname(__file__), 'input03.txt'), 'r+') as f:
      for l in f.readlines():
        diagnostics.append(list(l.strip()))
    return diagnostics

def execute_part_2():
  diagnostics = read_input()

  o2_generator_rating, co2_scrubber_rating = get_rating(diagnostics, most_common=True, idx=0, tie_breaker='1'), get_rating(diagnostics, most_common=False, idx=0, tie_breaker='0')

  print(f'Oxygen rating: {o2_generator_rating}, CO2 rating: {co2_scrubber_rating}. Life support rating: {o2_generator_rating*co2_scrubber_rating}.')

def get_most_common(counter, most_common, tie_breaker):
  if counter.most_common(1)[0][1] == counter.most_common(2)[1][1]:
    return tie_breaker
  
  mc = counter.most_common(1)[0][0]
  return mc if most_common else str(1-int(mc))

def get_rating(diagnostics, most_common, idx, tie_breaker):
  diag_counter = get_counter(diagnostics)

  counter = diag_counter[idx]
  mc = get_most_common(counter, most_common, tie_breaker)

  filtered_diagnostics = list(filter(lambda x: x[idx] == mc, diagnostics))

  if len(filtered_diagnostics) == 1:
    return int(''.join(filtered_diagnostics[0]), 2)

  return get_rating(filtered_diagnostics, most_common, idx+1, tie_breaker)


execute_part_2()