class Reader:

  @staticmethod
  def readline():
    import sys
    return sys.stdin.buffer \
      .readline().rstrip()


  @classmethod
  def read_int(cls):
    i = int(cls.readline())
    return i


  @classmethod
  def read_str(cls):
    s = cls.readline().decode()
    return s


  @classmethod
  def readline_ints(cls):
    *ints, = map(
      int,
      cls.readline().split(),
    )
    return ints


  @classmethod
  def readline_strs(cls):
    s = cls.read_str().split()
    return s


  @staticmethod
  def read():
    import sys
    i = sys.stdin.buffer.read()
    return i


  @classmethod
  def read_ints(cls):
    *ints, = map(
      int,
      cls.read().split(),
    )
    return ints


  @classmethod
  def read_strs(cls):
    return cls.read() \
      .decode().split()


  @staticmethod
  def readlines():
    import sys
    lines = sys.stdin.buffer \
      .readlines()
    lines = [
      l.rstrip()
      for l in lines
    ]
    return lines


class ReaderNumpy(Reader):

  @classmethod
  def readline_ints(cls):
    import numpy as np
    return np.fromstring(
      string=cls.read_str(),
      dtype=np.int64,
      sep=' ',
    )


  @classmethod
  def read_ints(cls):
    import numpy as np
    return np.fromstring(
      string=cls.read() \
        .decode(),
      dtype=np.int64,
      sep=' ',
    )


class Solver:

  def __init__(self):
    self.reader = Reader()
    # self.reader = ReaderNumpy()


  def __prepare(self):
    reader = self.reader
    n, m = \
      reader.readline_ints()
    self.n, self.m = n, m


  def __solve(self):
    n, m = self.n, self.m
    cnt = [0, 0, 0]
    if m & 1:
      m -= 3
      cnt[1] += 1
      n -= 1
    cnt[2] = m//2 - n
    cnt[0] = n - cnt[2]
    if any(c<0 for c in cnt):
      print(-1, -1, -1)
    else:
      print(*cnt, sep=' ')


  def run(self):
    self.__prepare()
    self.__solve()


def main():
  t = 1
  # t = Reader.read_int()
  for _ in range(t):
    solver = Solver()
    solver.run()


if __name__ == '__main__':
  main()
