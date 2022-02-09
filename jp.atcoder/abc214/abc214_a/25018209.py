def main():
  n = int(input())
  ans = (
    4 if n < 126 else
    6 if n < 212 else
    8
  )
  print(ans)


main()
