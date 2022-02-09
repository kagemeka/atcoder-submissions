import typing

def main() -> typing.NoReturn:
    s, t, x = map(int, input().split())
    ans = 'No'
    if s <= x < t:
        ans = 'Yes'
    if t < s <= x:
        ans = 'Yes'
    if x < t < s:
        ans = 'Yes'
    print(ans)
    # if s == 23: print('Yes')
    # print('Yes' if s <= x < t else 'No')


main()
