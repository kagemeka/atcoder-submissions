

def main():
  n = int(input())
  *s, = map(int, input().split())
  *t, = map(int, input().split())

  inf = 1 << 60

  for i in range(2 * n):
    i %= n
    j = (i + 1) % n
    t[j] = min(
      t[j],
      t[i] + s[i],
    )

  print(*t, sep='\n')



main()
