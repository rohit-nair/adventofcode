#! /usr/bin/env python3

import numpy as np
import pandas as pd
from os import path
import re

INPUT_PATTERN = r"<.=(\-?\d+), .=(\-?\d+), .=(\-?\d+)>"

def simulate(positions, velocities, steps=10):
  df_positions, df_velocities = pd.DataFrame(np.array(positions), columns=['x', 'y', 'z']),\
    pd.DataFrame(np.array(velocities), columns=['x', 'y', 'z'])

  for _ in range(steps):

    df_gravity = calculate_gravity(df_positions)
    df_velocities += df_gravity
    df_positions += df_velocities

  pot = df_positions.abs().sum(1)
  kin = df_velocities.abs().sum(1)

  return sum(pot*kin)

def calculate_gravity(df):
  rows, columns = df.shape
  res = pd.DataFrame(index=df.index, columns=df.columns)
  res[:] = 0

  for i, row in df.iterrows():
    greater_than = df.iloc[list(set(range(rows)) - set([i])),:].gt(row,axis=1).sum(axis=0)
    less_than = df.iloc[list(set(range(rows)) - set([i])),:].lt(row,axis=1).sum(axis=0)
    res.iloc[i,:] = greater_than - less_than

  return res



def get_inputs(file='testinput12.txt'):
  position, velocity = [], []
  with open(path.join(path.dirname(__file__),file), 'r+') as f:
    for l in f.readlines():
      matches = re.match(INPUT_PATTERN, l.rstrip('\r').rstrip('\n'))
      position.append(list(map(int, matches.groups())))
      velocity.append([0, 0, 0])
  return position, velocity

if __name__ == '__main__':
  print(simulate(*get_inputs('input12.txt'), 1000))
  # assert simulate(*get_inputs(), 100) == 1940, 'Assertion failed.'
