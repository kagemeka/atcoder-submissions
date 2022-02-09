import typing


def main():
  s, t = map(int, input().split())

  cnt = 0
  for i in range(s + 1):
    for j in range(s - i + 1):
      for k in range(s - i - j + 1):
        a = i + j + k
        b = i * j * k
        cnt += a <= s and b <= t

  print(cnt)


main()
