import sys
from collections import Counter

s = sys.stdin.readline().rstrip()

def main():
    for c in Counter(s).values():
        if c & 1:
            return 'No'

    return 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)
