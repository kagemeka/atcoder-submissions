from __future__ import annotations
import typing
import heapq
import dataclasses



@dataclasses.dataclass
class DoublyLinkedListNode():
  value: typing.Optional[typing.Any] = None
  left: typing.Optional[DoublyLinkedListNode] = None
  right: typing.Optional[DoublyLinkedListNode] = None



@dataclasses.dataclass
class DoublyLinkedList():
  first: typing.Optional[DoublyLinkedListNode] = None
  last: typing.Optional[DoublyLinkedListNode] = None



class Deque():
  def __init__(
    self,
  ) -> typing.NoReturn:
    self.__first: typing.Optional[DoublyLinkedListNode] = None
    self.__last: typing.Optional[DoublyLinkedListNode] = None


  def append(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    x = DoublyLinkedListNode(value=v, left=self.__last)
    if x.left is None:
      self.__first = x
    else:
      self.__last.right = x
    self.__last = x


  def appendleft(
    self,
    v: typing.Any,
  ) -> typing.NoReturn:
    x = DoublyLinkedListNode(value=v, right=self.__first)
    if self.__right is None:
      self.__last = x
    else:
      self.__first.left = x
    self.__first = x


  def pop(
    self,
  ) -> typing.Any:
    if self.__last is None:
      raise Exception('cannot pop from empty deque.')
    v = self.__last.value
    self.__last = self.__last.left
    if self.__last is None:
      self.__first = None
    else:
      self.__last.right = None
    self.__last.right = None
    return v


  def popleft(
    self,
  ) -> typing.Any:
    if self.__first is None:
      raise Exception('cannot pop from empty deque.')
    v = self.__first.value
    self.__first = self.__first.right
    if self.__first is None:
      self.__last = None
    else:
      self.__first.left = None
    return v


  def __bool__(self) -> bool:
    return self.__first is not None



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
