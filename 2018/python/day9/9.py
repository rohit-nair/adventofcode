#! /usr/bin/env python3

def gethighscore(nbrplayers, lastmarble):
  idx, i, player, playerscore, circle = 0, 1, 1, [0 for i in range(nbrplayers)], [0]
  while i <= lastmarble:
    if i % 23 == 0:
      playerscore[player] += i
      idx = idx - 7 if idx > 6 else (len(circle) - 1) - (7-(idx+1))
      playerscore[player] += circle[idx]
      del circle[idx]
    else:
      idx = (idx + 2)%len(circle)
      if idx == 0:
        circle.append(i)
        idx = len(circle) - 1
      else:
        circle.insert(idx, i)
  
    i, player = i + 1, (player + 1)%nbrplayers
  
  print("Max score", max(playerscore))
  return circle, max(playerscore)

assert gethighscore(9, 25) == ([0, 16, 8, 17, 4, 18, 19, 2, 24, 20, 25, 10, 21, 5, 22, 11, 1, 12, 6, 13, 3, 14, 7, 15], 32), "Didn't match test case 1."
assert gethighscore(10, 1618)[1] == 8317, "Didn't match test case 2."
assert gethighscore(13, 7999)[1] == 146373, "Didn't match test case 3."
assert gethighscore(17, 1104)[1] == 2764, "Didn't match test case 4."
assert gethighscore(21, 6111)[1] == 54718, "Didn't match test case 5."
assert gethighscore(30, 5807)[1] == 37305, "Didn't match test case 6."

print('Solution is: ', gethighscore(416, 71975)[1])
print('Solution for 100 times larger last marble is: ', gethighscore(416, 7197500)[1])