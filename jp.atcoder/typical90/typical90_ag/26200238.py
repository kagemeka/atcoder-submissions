import typing


def main() -> typing.NoReturn:
  h, w = map(int, input().split())
  if h == 1 or w == 1:
    print(h * w)
    return
  mx = 1
  mx *= (h + 1) // 2
  mx *= (w + 1) // 2
  print(mx)


main()
