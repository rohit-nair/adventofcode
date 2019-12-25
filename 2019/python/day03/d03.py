#! /usr/bin/env python3

def get_input(file='testinput03.txt'):
  with open(file, 'r+') as f:
    # print(f.readline().split(','))
    return list(map(lambda l: l.rstrip('\r').rstrip('\n').split(','),
      f.readlines()))

def get_path(direction):
  x, y, path = 0, 0, set()
  
  for d in direction:
    orient, spacing = d[0], int(d[1:])
    if orient == 'U':
      for step in range(1, spacing+1):
        path.add((x,y+step))
      y += spacing
    elif orient == 'D':
      for step in range(1, spacing+1):
        path.add((x,y-step))
      y -= spacing
    elif orient == 'R':
      for step in range(1, spacing+1):
        path.add((x+step,y))
      x += spacing
    elif orient == 'L':
      for step in range(1, spacing+1):
        path.add((x-step,y))
      x -= spacing
    else:
      raise RuntimeError('Invalid orientation.')

  return path

def find_closest_intersect(intersection):
  closest = float('inf')
  for x, y in intersection:
    dist = abs(x) + abs(y)
    if dist < closest:
      closest = dist
  return closest

direction1, direction2 = get_input()
path1, path2 = get_path(direction1), get_path(direction2)

assert find_closest_intersect(path1.intersection(path2)) == 135, 'Assertion failed.'

d1, d2 = get_input('input03.txt')
p1, p2 = get_path(d1), get_path(d2)
print(f'Closest intersection point is {find_closest_intersect(p1.intersection(p2))} distance away.')

