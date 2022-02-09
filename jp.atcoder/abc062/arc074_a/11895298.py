import sys

def solve(h, w):
  res = [((h + 2) // 3 - h // 3) * w]
  for d in [h // 3, (h + 2) // 3]:
    cand = sorted([d * w, (h - d) * (w // 2), (h - d) * ((w + 1) // 2)])
    res.append(cand[-1] - cand[0])
  return min(res)

h, w = map(int, sys.stdin.readline().split())

def main():
  print(min(solve(h, w), solve(w, h)))

if __name__ == '__main__':
  main()
