import typing


def main() -> typing.NoReturn:
  s = input()
  t = input()
  n, m = len(s), len(t)

  dp0 = [''] * (m + 1)
  for i in range(n):
    dp1 = [''] * (m + 1)
    x = s[i]
    for j in range(m):
      y = t[j]
      if y == x:
        dp1[j + 1] = dp0[j] + y
        continue
      y = dp0[j + 1]
      z = dp1[j]
      dp1[j + 1] = (
        dp1[j]
        if len(z) >= len(y)
        else dp0[j + 1]
      )
    dp0 = dp1
  print(dp1[-1])


main()
