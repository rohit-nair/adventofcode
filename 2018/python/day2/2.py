#! /usr/bin/env python3

from collections import defaultdict
from collections import Counter

def findchecksum(fileloc = 'test_input.txt'):
    '''
        rtype: int, returns checksum
    '''
    checksum = (0,0)
    with open(fileloc, 'r') as f:
        for l in f.readlines():
            checksum = tuple((sum(x) for x in zip(checksum, findchecksumtxt(l.rstrip('\n')))))

    return checksum[0]*checksum[1]

def findchecksumtxt(txt):
    occurences = Counter(txt)
    twos, threes = False, False
    for k in list(occurences):
        threes |= bool(occurences[k] // 3)
        twos |= bool((occurences[k] % 3) // 2)
    return tuple(map(int, (twos, threes)))



if __name__ == '__main__':
    # assert findchecksumtxt('nkucgflathzwsicxrevtmbtpoq') ==(1,1), "Yo watch out."
    print('Check sum is:', findchecksum('input.txt'))