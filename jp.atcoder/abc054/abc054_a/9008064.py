import sys

a, b = map(int, sys.stdin.readline().split())

def strongness(x):
    return (x + 11) % 13

def main():
    sa = strongness(a)
    sb = strongness(b)
    if sa == sb:
        return 'Draw'
    elif sa > sb:
        return 'Alice'
    else:
        return 'Bob'


if __name__ == '__main__':
    ans = main()
    print(ans)
