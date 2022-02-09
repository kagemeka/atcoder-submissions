import sys

s = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline().rstrip())
n = len(s)

def main():
    res = set()
    for i in range(n):
        for j in range(i, n):
            res.add(s[i:j+1])
    return sorted(res)[k-1]

if __name__ == '__main__':
    ans = main()
    print(ans)
