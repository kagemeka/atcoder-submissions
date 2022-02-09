import typing



def is_choku(s: str) -> bool:
  if not s: return True
  if s[-2:] == 'ch' and is_choku(s[:-2]): return True
  if s[-1:] in set('oku') and is_choku(s[:-1]): return True
  return False



def main() -> typing.NoReturn:
  x = input()
  ans = 'YES' if is_choku(x) else 'NO'
  print(ans)


main()
