import typing
import collections

def main() -> typing.NoReturn:
    n = int(input())
    s = [input() for _ in range(n)]
    count = sorted(collections.Counter(s).items(), key=lambda x: -x[1])
    print(count[0][0])

main()
