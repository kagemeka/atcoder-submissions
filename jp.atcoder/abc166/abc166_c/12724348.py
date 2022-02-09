import sys

n, m = map(int, sys.stdin.readline().split())
*h, = map(int, sys.stdin.readline().split())

surround = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1; b -= 1
    surround[a].append(h[b])
    surround[b].append(h[a])

def main():
    cnt = 0
    for i in range(n):
        try:
            if h[i] > max(surround[i]):
                cnt += 1
        except:
            cnt += 1
    print(cnt)
if __name__ == '__main__':
  main()
