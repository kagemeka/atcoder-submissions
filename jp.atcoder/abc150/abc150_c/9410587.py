import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
p, q = [tuple(map(int, sys.stdin.readline().split())) for _ in range(2)]

def main():
    perms = list(permutations(range(1, n+1)))
    return abs(perms.index(p) - perms.index(q))

if __name__ == '__main__':
    ans = main()
    print(ans)
