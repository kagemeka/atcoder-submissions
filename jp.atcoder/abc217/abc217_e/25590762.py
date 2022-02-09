import typing
import heapq
import collections



def main() -> typing.NoReturn:
  n = int(input())
  hq = []
  queue = collections.deque()
  top = None
  for _ in range(n):
    *q, = map(int, input().split())
    if q[0] == 1:
      x = q[1]
      queue.append(x)
    elif q[0] == 2:
      x = heapq.heappop(hq) if hq else queue.popleft()
      print(x)
    elif q[0] == 3:
      while queue:
        x = queue.popleft()
        heapq.heappush(hq, x)


main()
