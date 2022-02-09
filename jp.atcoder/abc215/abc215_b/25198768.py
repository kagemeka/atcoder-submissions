import typing


def main():
  n = int(input())
  x = 1
  cnt = 0
  while True:
    if x * 2 > n: break
    cnt += 1
    x *= 2
  print(cnt)


main()
