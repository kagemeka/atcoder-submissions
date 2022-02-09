import sys

n = int(sys.stdin.readline().rstrip())
xy = [[] for _ in range(n)]
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    for j in range(a):
        x, y = map(int, sys.stdin.readline().split())
        xy[i].append((x-1, y))

def main():
    ans = 0
    for comb in range(2 ** n):
        cnt = 0
        for i in range(n):
            if comb >> i & 1 ^ 1:
                continue
            for x, y in xy[i]:
                if comb >> x & 1 ^ y:
                    break
            else:
                cnt += 1
                continue
            break
        else:
            ans = max(ans, cnt)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
