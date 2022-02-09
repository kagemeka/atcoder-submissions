import sys

s = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline().rstrip())
n = len(s)

def main():
    res = set()
    for l in range(n):
        for r in range(l, min(l+k, n)):
            res.add(s[l:r+1])

    return sorted(res)[k-1]

if __name__ == '__main__':
    ans = main()
    print(ans)
