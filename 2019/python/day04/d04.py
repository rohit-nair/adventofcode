#! /usr/bin/env python3

def check_criteria(numb):
  if len(str(numb)) != 6:
    return False
  
  x1, x2, x3, x4, x5, x6 = str(numb)
  if not (x1 <= x2 <= x3 <= x4 <= x5 <= x6):
    return False

  if not ((x1 == x2 and x1 not in (x3, x4, x5, x6)) 
    or (x2 == x3 and x2 not in (x1, x4, x5, x6))
    or (x3 == x4 and x3 not in (x1, x2, x5, x6))
    or (x4 == x5 and x4 not in (x1, x2, x3, x6))
    or (x5 == x6 and x5 not in (x1, x2, x3, x4))):
    return False
  
  return True

def brute_force(start_nbr, end_nbr):
  return [x for x in range(start_nbr, end_nbr+1) if check_criteria(x)]

print(f'Number of potential passwords: {len(brute_force(264793, 803935))}')