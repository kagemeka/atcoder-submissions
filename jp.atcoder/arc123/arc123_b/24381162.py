import sys



def read_ints():
  a = sys.stdin.readline()
  *a, = map(int, a.split())
  return a


def main():
  n = int(input())
  a = sorted(read_ints())
  b = sorted(read_ints())
  c = sorted(read_ints())

  i = j = k = 0
  cnt = 0

  while i < n:
    while j < n:
      if b[j] > a[i]: break
      j += 1
    else: break

    while k < n:
      if c[k] > b[j]: break
      k += 1
    else: break

    cnt += 1
    i += 1
    j += 1
    k += 1

  print(cnt)


main()
