#! /usr/bin/env python

elf1, elf2 = 0, 1
state = [3, 7]

def createnewrecipe():
  global elf1, elf2
  elf1score, elf2score = state[elf1], state[elf2]
  newscore = elf1score+elf2score
  state.extend(map(int, list(str(newscore))))
  elf1 = (elf1+elf1score+1)%len(state)
  elf2 = (elf2+elf2score+1)%len(state)
  # print(''.join(map(str, state)))

def printscores():
  res = ''
  if len(state) > 10:
    for i in range(len(state)-11):
      # print('Recipe {:0>4d}, score: {}'.format(i+1, ''.join(map(str, state[i+1:i+11]))))
      res += 'Recipe {:0>4d}, score: {}.\n'.format(i+1, ''.join(map(str, state[i+1:i+11])))

  with open('14res.txt', 'w+') as f:
    f.writelines(res)

while not ''.join(map(str, state[-6:])) == "899611":
  createnewrecipe()

# printscores()

print('The score 899611 appears after {} recipes'.format(len(state) - 6))


