import typing


def query(u: int, v: int) -> int:
  s = f'? {u} {v}'
  print(s, flush=True)
  return int(input())


def main() -> typing.NoReturn:
  n = int(input())

  def find_farest(u: int) -> typing.Tuple[int, int]:
    mx = 0
    v = -1
    for i in range(1, n + 1):
      d = query(u, i)
      if d <= mx: continue
      mx = d
      v = i
    return v, mx

  u, _ = find_farest(1)
  _, d = find_farest(u)
  print(f'! {d}')


main()
