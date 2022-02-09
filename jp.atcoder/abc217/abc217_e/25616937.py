import typing
import heapq


class FIFOQueue():
  def __bool__(self) -> bool:
    return self.__i < len(self.__a)


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__a = []
    self.__i = 0


  def append(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    self.__a.append(v)


  def pop(
    self,
  ) -> typing.Any:
    v = self.__a[self.__i]
    self.__i += 1
    return v


def main() -> typing.NoReturn:
  n = int(input())
  hq = []
  ffq = FIFOQueue()
  for _ in range(n):
    *q, = map(int, input().split())
    if q[0] == 1:
      x = q[1]
      ffq.append(x)
    elif q[0] == 2:
      x = heapq.heappop(hq) if hq else ffq.pop()
      print(x)
    elif q[0] == 3:
      while ffq:
        x = ffq.pop()
        heapq.heappush(hq, x)


main()
