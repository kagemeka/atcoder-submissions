from __future__ import annotations
import typing
import heapq
import dataclasses



@dataclasses.dataclass
class SinglyLinkedListNode():
  value: typing.Optional[typing.Any] = None
  next: typing.Optional[SinglyLinkedListNode] = None



class FIFOQueue():
  def __bool__(self) -> bool:
    return self.__first is not None


  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__first: typing.Optional[SinglyLinkedListNode] = None
    self.__last: typing.Optional[SinglyLinkedListNode] = None


  def append(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    x = SinglyLinkedListNode(value=v)
    if self.__last is None:
      self.__first = x
    else:
      self.__last.next = x
    self.__last = x


  def pop(
    self,
  ) -> typing.Any:
    if self.__first is None:
      raise Exception('cannot pop from empty queue.')
    v = self.__first.value
    self.__first = self.__first.next
    if self.__first is None:
      self.__last = None
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
