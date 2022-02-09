import sys

n, k = map(int, sys.stdin.readline().split())

def main():
  m = n - 1
  cnt = (n - 1) * (n - 2) // 2
  if k > cnt: print(-1); return
  edges = [(1, v) for v in range(2, n + 1)]

  for u in range(2, n):
    for v in range(u + 1, n + 1):
      if cnt == k: break
      edges.append((u, v))
      m += 1
      cnt -= 1

  print(m)
  for u, v in edges:
    print(u, v)

if __name__ == '__main__':
  main()
