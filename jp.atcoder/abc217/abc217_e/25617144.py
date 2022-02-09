import typing
import heapq


class Deque():
  def __bool__(self) -> bool:
    return self.__l <= self.__r


  def __init__(
    self,
    max_size: int = 1 << 20,
  ) -> typing.NoReturn:
    self.__a = [None] * max_size
    self.__l = 0
    self.__r = -1


  def append(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    self.__r += 1
    self.__a[self.__r] = v


  def appendleft(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    self.__l -= 1
    self.__a[self.__l] = v


  def empty(self) -> bool:
    return not bool(self)


  def pop(
    self,
  ) -> typing.Any:
    if self.empty():
      raise Exception('cannot pop from empty deque.')
    v = self.__a[self.__r]
    self.__r -= 1
    return v


  def popleft(
    self,
  ) -> typing.Any:
    if self.empty():
      raise Exception('cannot pop from empty deque.')
    v = self.__a[self.__l]
    self.__l += 1
    return v



def main() -> typing.NoReturn:
  n = int(input())
  hq = []
  dq = Deque()
  for _ in range(n):
    *q, = map(int, input().split())
    if q[0] == 1:
      x = q[1]
      dq.append(x)
    elif q[0] == 2:
      x = heapq.heappop(hq) if hq else dq.popleft()
      print(x)
    elif q[0] == 3:
      while dq:
        x = dq.popleft()
        heapq.heappush(hq, x)


main()
