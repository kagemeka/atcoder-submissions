import typing
import sys


def rotate90(
  a: typing.List[typing.Tuple[str]],
) -> typing.List[typing.Tuple[str]]:
  return list(''.join(s) for s in zip(*a[::-1]))



def main() -> typing.NoReturn:
  c = [input() for _ in range(4)]
  c = '\n'.join(rotate90(rotate90(c)))
  print(c)


main()
