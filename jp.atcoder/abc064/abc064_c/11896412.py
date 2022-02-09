import sys

n, *a = map(int, sys.stdin.read().split())

def main():
  cnt = [0] * 9
  for x in a:
    cnt[min(x, 3200) // 400] += 1
  mi = 0
  for x in cnt[:8]:
    if x: mi += 1
  ma = mi + cnt[8]
  mi = max(1, mi)
  print(mi, ma)

if __name__ == '__main__':
  main()
