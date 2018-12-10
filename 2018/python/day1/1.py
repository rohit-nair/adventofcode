#! /usr/bin/env python3

with open('1_input.txt', 'r') as f:
    read_data = [int(l.rstrip('\n')) for l in f.readlines()]

print 'Sum of frequencies is: ', sum(read_data)

visitedfreq = set([])
currentfreq = 0
hasfreqrepeated = False

while not hasfreqrepeated:
    for f in read_data: 
        currentfreq += f 
        if currentfreq in visitedfreq:
                print "Found repeating frequency: ", currentfreq
                hasfreqrepeated = True
                break
        visitedfreq.add(currentfreq)
