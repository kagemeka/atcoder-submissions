import sys
from itertools import permutations

a = tuple(int(x) for x in sys.stdin.readline().split())

def main():
    for p in set(permutations([5, 5, 7], 3)):
        if a == p:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
