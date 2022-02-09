import sys
from collections import defaultdict

s, t = sys.stdin.read().split()
n = len(s)

def main():
    correspondence = defaultdict(str)
    for i in range(n):
        if not correspondence[s[i]]:
            correspondence[s[i]] = t[i]
        else:
            if correspondence[s[i]] != t[i]:
                return 'No'

    v = correspondence.values()
    return 'Yes' if len(v) == len(set(v)) else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
