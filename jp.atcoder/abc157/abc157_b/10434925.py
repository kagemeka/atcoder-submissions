import sys

a = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
n, *b = map(int, sys.stdin.read().split())
b = set(b)

def main():
    res = [[False] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            if a[i][j] in b:
                res[i][j] = True

    for i in range(3):
        for j in range(3):
            if not res[i][j]:
                break
        else:
            return 'Yes'

    for j in range(3):
        for i in range(3):
            if not res[i][j]:
                break
        else:
            return 'Yes'

    for i, j in zip(range(3), range(3)):
        if not res[i][j]:
            break
        else:
            return 'Yes'

    for i, j in zip(range(3), range(2, -1, -1)):
        if not res[i][j]:
            break
        else:
            return 'Yes'

    return 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
