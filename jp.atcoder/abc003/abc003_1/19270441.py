class StdinReader:

  @staticmethod
  def readline():
    import sys
    return sys.stdin.buffer \
      .readline().rstrip()


  @classmethod
  def read_int(cls):
    return int(cls.readline())


  @classmethod
  def readline_ints(cls):
    *ints, = map(
      int,
      cls.readline().split(),
    )
    return ints


  # @classmethod
  # def readline_ints(cls):
  #   import numpy as np
  #   return np.fromstring(
  #     string=cls.readline() \
  #       .decode(),
  #     dtype=np.int64,
  #     sep=' ',
  #   )


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


  # @classmethod
  # def read_ints(cls):
  #   import numpy as np
  #   return np.fromstring(
  #     string=cls.read() \
  #       .decode(),
  #     dtype=np.int64,
  #     sep=' ',
  #   )


  @staticmethod
  def readlines():
    import sys
    return sys.stdin.buffer \
      .readlines()


class Solver:

  def __init__(self):
    ...


  def __prepare(self):
    sr = StdinReader()
    self.n = sr.read_int()


  def __solve(self):
    n = self.n
    salary = (n + 1) * 5000
    print(salary)


  def run(self):
    self.__prepare()
    self.__solve()


def main():
  t = 1
  # t = StdinReader.read_int()
  for _ in range(t):
    solver = Solver()
    solver.run()


if __name__ == '__main__':
  main()
