import typing


def main():
  s, t = map(int, input().split())


  cnt = 0
  for i in range(101):
    for j in range(101):
      for k in range(101):
        a = i + j + k
        b = i * j * k
        cnt += a <= s and b <= t

  print(cnt)



main()
