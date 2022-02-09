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


  def round_time(self, s, e):
    s = s // 5 * 5
    e = (e + 4) // 5 * 5
    return s, e


  def __prepare(self):
    reader = self.reader
    n = reader.read_int()
    self.n = n
    m = 24 * 60 + 1
    term = [0] * (m + 1)
    for _ in range(n):
      se = reader.read_str()
      se = map(
        int,
        se.split('-')
      )
      s, e = map(
        self.to_minutes,
        se,
      )
      s, e = self.round_time(
        s, e)

      term[s] += 1
      term[e+1] -= 1

    for i in range(m):
      term[i+1] += term[i]

    self.term = term
    self.m = m


  @staticmethod
  def to_minutes(t):
    q, r = divmod(t, 100)
    return 60 * q + r


  @staticmethod
  def to_hmform(t):
    q, r = divmod(t, 60)
    return 100 * q + r


  def __solve(self):
    n, m = self.n, self.m
    term = self.term

    res = []
    raining = False
    for i in range(m + 1):
      if term[i]:
        if raining: continue
        s = i
        raining = True
      elif raining:
        res.append((s, i-1))
        raining = False

    for se in res:
      s, e = map(
        self.to_hmform,
        se,
      )
      print(f'{s:04}-{e:04}')


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
