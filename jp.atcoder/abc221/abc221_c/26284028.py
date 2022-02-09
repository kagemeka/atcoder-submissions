import typing



def main() -> typing.NoReturn:

  n = input()
  m = len(n)


  mx = 0
  for s in range(1 << m):
    a = []
    b = []
    for i in range(m):
      if s >> i & 1:
        a.append(n[i])
      else:
        b.append(n[i])
    if not b or not a: continue
    a.sort()
    b.sort()
    a = int(''.join(a)[::-1])
    b = int(''.join(b)[::-1])
    mx = max(mx, a * b)

  print(mx)

main()
