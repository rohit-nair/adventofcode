#!/usr/bin/env python
import re, heapq
from collections import defaultdict, OrderedDict

p = r"Step (.) must be finished before step (.) can begin."

def getinput(file='testinput7.txt'):
  with open(file, 'r+') as f:
    return [re.match(p, l.rstrip('\n')).groups() for l in f.readlines()]

def getgraph(input):
  g = defaultdict(set)
  for d in input:
    g[d[0]].add(d[1])
  return g

def getdpendencygraph(input):
  g = defaultdict(set)
  for d in input:
    g[d[1]].add(d[0])
  return g

def printgraph(g):
  print('\n'.join(sorted([str((k, v)) for k, v in g.items()])))

def topologicalsort(g):
  # printgraph(g)
  visited, order = set(), []
  for v in sorted(g.keys(), reverse=True):
    dfs(g, v, visited, order)
  return ''.join(list(reversed(order)))

def dfs(g, v, visited, order):
  # print(v)
  if v in g.keys():
    for c in sorted(list(g[v]), reverse=True):
      if c in visited:
        continue
      dfs(g, c, visited, order)
  if v not in visited:
    visited.add(v)
    order.append(v)
  pass


def calculateexectime(input, nworkers=2, basetime=0):
  executiontime, g = 0, getgraph(input)
  dg, order = getdpendencygraph(input), topologicalsort(g)
  jobs = set(list(order)[:])
  jobsassigned, jobscompleted, availablejobs, workers = set(), set(), OrderedDict(), []
  
  while not len(jobscompleted) == len(order):
    # find completed job and reduce it's time from 
    # other jobs already with workers
    if len(workers) > 0:
      cj = heapq.heappop(workers)
      if cj:
        for j in workers:
          j[0] -= cj[0]
      jobscompleted.add(cj[1])
      jobsassigned.remove(cj[1])
      executiontime += cj[0]

    getavailablejobs(availablejobs, g, dg, jobs, jobsassigned, jobscompleted)
    for aj in list(availablejobs):
      if len(workers) < nworkers:
        heapq.heappush(workers, [timetoexecute(aj, basetime), aj])
        del availablejobs[aj]
        jobsassigned.add(aj)
        jobs.remove(aj)
  return executiontime

def timetoexecute(job, basetime = 0):
  return basetime + ord(job) - ord('A') + 1


def getavailablejobs(availablejobs, g, dg, jobs, jobsassigned, jobscompleted):
  for j in jobs - jobsassigned.union(jobscompleted, set(availablejobs.keys())):
    if alldependenciescompleted(dg[j], jobscompleted):
      availablejobs[j] = True
  pass

def alldependenciescompleted(depends, jobscompleted):
  return all(True if d in jobscompleted else False for d in depends)


# t = topologicalsort(getgraph(getinput('testinput7.txt')))
# print(t)
# print(calculateexectime(getinput('testinput7.txt')))
print(calculateexectime(getinput('input7.txt'), 5, 60))