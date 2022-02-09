import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

def main():
    cnt = [0] * 3
    for c in s:
      if c == 'R': cnt[0] += 1
      elif c == 'G': cnt[1] += 1
      else: cnt[2] += 1
    res = cnt[0] * cnt[1] * cnt[2]
    for i in range(n - 2):
      for j in range(i + 1, n - 1):
        k = 2 * j - i
        if k >= n: break
        res -= s[i] != s[j] and s[j] != s[k] and s[k] != s[i]
    print(res)

if __name__ == '__main__':
  main()
