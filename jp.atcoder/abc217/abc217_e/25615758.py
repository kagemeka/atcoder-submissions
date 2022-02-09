from __future__ import annotations
import typing
import heapq
import collections


import dataclasses


@dataclasses.dataclass
class Node():
  value: typing.Optional[typing.Any] = None
  left: typing.Optional[Node] = None
  right: typing.Optional[Node] = None




@dataclasses.dataclass
class DoublyLinkedList():
  first: typing.Optional[Node] = None
  last: typing.Optional[Node] = None



class Deque():
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__a = DoublyLinkedList()


  def append(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    a = self.__a
    x = Node(value=v, left=a.last)
    if x.left is None:
      a.first = x
    else:
      a.last.right = x
    a.last = x


  def appendleft(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    a = self.__a
    x = Node(value=v, right=a.first)
    if x.right is None:
      a.last = x
    else:
      a.first.left = x
    a.first = x


  def pop(
    self,
  ) -> typing.Any:
    a = self.__a
    if a.last is None:
      raise Exception('cannot pop from empty deque.')
    v = a.last.value
    a.last = a.last.left
    if a.last is None:
      a.first = None
    else:
      a.last.right = None
    a.last.right = None
    return v


  def popleft(
    self,
  ) -> typing.Any:
    a = self.__a
    if a.first is None:
      raise Exception('cannot pop from empty deque.')
    v = a.first.value
    a.first = a.first.right
    if a.first is None:
      a.last = None
    else:
      a.first.left = None
    return v


  def __bool__(self) -> bool:
    a = self.__a
    return a.first is not None


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
