import sys

def strongness(x):
    return (x + 11) % 13

a, b = map(int, sys.stdin.readline().split())
a = strongness(a)
b = strongness(b)

def main():
    if a > b: ans = 'Alice'
    elif a == b: ans = 'Draw'
    else: ans = 'Bob'
    print(ans)

if __name__ ==  '__main__':
    main()
