# import sys
# input = sys.stdin.readline

N, *a = [int(x) for x in open(0)]
a.insert(0, None)

first = 1
pres = first
count = 0
nex =  a[pres] # press the button
count += 1
for i in range(N-1): # operations are at most N-1 times.
    if nex == 2: break
    prev = pres
    pres = nex
    nex = a[pres] # press the button
    count += 1
    if nex == prev or nex == pres: break

if nex == 2: print(count)
else: print(-1)
