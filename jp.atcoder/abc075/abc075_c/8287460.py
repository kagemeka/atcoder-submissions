import sys
from collections import Counter
n, m, *ab = (int(x) for x in sys.stdin.read().split())

bridges = 0
still_exist = True
while still_exist:
    bef = len(ab)
    for vertex, edges_count in Counter(ab).items():
        if edges_count == 1:
            i = ab.index(vertex)
            if i % 2 == 0: del ab[i:i+2]
            else: del ab[i-1:i+1]
            bridges += 1
            break
    aft = len(ab)
    if bef == aft: still_exist = False

print(bridges)
