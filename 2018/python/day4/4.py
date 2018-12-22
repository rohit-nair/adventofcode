#! /usr/bin/env python

import re
from enum import Enum

pattern = r"\[(.*) (\d+):(\d+)\] ((Guard #(\d+) begins shift)|((falls|wakes)? .*))"

class fragments(Enum):
  DATE = 0
  HOUR = 1
  MINUTE = 2
  SUBPART = 3
  GUARDID = 5
  ACTION = 7

def getInput(file="testinput.txt"):
  with open(file, 'r') as f:
    input = [re.match(pattern, l.rstrip('\n')).groups() for l in f.readlines()]
    return sorted(input, key = lambda x: (x[0], x[1], x[2]))

def findSleepyGuard(file='testinput.txt'):
  input = getInput(file)
  
  tracker, guardId, sleepStart, sleepEnd, mv, mguardid = {}, None, 0, 0, 0, None
  for i in input:
    if i[fragments.ACTION.value] == 'falls':
      sleepStart = int(i[fragments.MINUTE.value])
    elif i[fragments.ACTION.value] == 'wakes':
      sleepEnd = int(i[fragments.MINUTE.value])
      delta = sleepEnd-sleepStart
      if not guardId in tracker.keys():
        tracker[guardId] = [0,[0 for i in range(60)]]
      tracker[guardId][0] += delta
      if tracker[guardId][0] > mv:
        mv = tracker[guardId][0]
        mguardid = guardId
      for i in range(sleepStart, sleepEnd):
        tracker[guardId][1][i] += 1
    else:
      guardId = i[fragments.GUARDID.value]

  return int(mguardid) * getOptimalTime(tracker, mguardid), getMostFrequentMinuteSlept(tracker)

def getOptimalTime(tracker, mguardid):
  return tracker[mguardid][1].index(max(tracker[mguardid][1]))

def getMostFrequentMinuteSlept(tracker):
  mguardid, mmin, themin = None, 0, 0
  for k in tracker.keys():
    v = tracker[k]
    m = v[1].index(max(v[1]))
    if v[1][m] > mmin:
      themin, mmin, mguardid = m, v[1][m], k
  return int(mguardid) * themin


print(findSleepyGuard('input.txt')) 