#! /usr/bin/env python3

sheet = [[set() for i in range(1000)] for j in range(1000)]

def getinput(file='testinput.txt'):
  with open(file, 'r') as f:
    return [[i[0], list(map(int, i[2].rstrip(':').split(','))), \
    list(map(int, i[3].rstrip(':').split('x')))] \
    for i in [l.rstrip('\n').split() for l in f.readlines()]]

def getoverlappingregion(file='testinput.txt'):
  ids, input = set(), getinput(file)
  

  for idx, [j, i], [w, h] in input:
    ids.add(idx)
    for k in range(w):
      for l in range(h):
        sheet[i+l][j+k].add(idx)
  
  # return sum([sum([len(v)>1 for v in row]) for row in sheet])
  sqin = 0
  for i in range(len(sheet)):
    for j in range(len(sheet[0])):
      if len(sheet[i][j]) > 1:
        sqin += 1
        ids -= sheet[i][j]

  return sqin, ids


def isoverlap(i, j):
  return True if sheet[i][j] == 2 and \
      sheet[i+1][j] == 2 and \
      sheet[i][j+1] == 2 and \
      sheet[i+1][j+1] == 2 else False

# assert getinput()==[[[1, 3], [4, 4]], [[3, 1], [4, 4]], [[5, 5], [2, 2]]], "Input read incorrecty."

# assert getoverlappingregion() == 4, "Test case failed."

print("Overlapping regions size and the region that doesn't overlap is: ", getoverlappingregion('input.txt'))