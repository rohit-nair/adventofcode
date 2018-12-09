
def getinput(file="testinput.txt"):
  with open(file, 'r') as f:
    return list(map(int, f.readlines()[0].rstrip('\n').split(' ')))

def calculatesum(file="testinput.txt"):
  input = getinput(file)
  idx, summetadata = calculatesumnode(input, 0, 0)
  print('####Results####\nInput lenght: {} | Final index: {} | Sum metadata: {}.'.format(len(input), idx, summetadata))

def calculatesumnode(input, idx, summetadata):
  valuechildnodes, nbrchild, nbrmetadata = [], input[idx], input[idx+1]
  idx = idx + 2 # forward to next node or metadata

  if nbrchild == 0:
    idx, summetadata = idx + nbrmetadata, summetadata + sum(input[idx:idx+nbrmetadata])
    return idx, summetadata

  for i in range(nbrchild):
    idx, valchildnode = calculatesumnode(input, idx, summetadata)
    valuechildnodes.append(valchildnode)

  for i in input[idx:idx+nbrmetadata]:
    if i > len(valuechildnodes):
      continue

    summetadata = summetadata + valuechildnodes[i-1]

  idx = idx + nbrmetadata

  return idx, summetadata



if __name__ == "__main__":
  # assert len(getinput()) == 16, "Input incorrectly parsed."
  # calculatesum()
  calculatesum("input.txt")