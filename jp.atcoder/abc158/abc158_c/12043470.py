import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    res = -1
    for i in range(1, 2000):
        if i * 8 // 100 == a and i // 10 == b:
            res = i
            break
    print(res)

if __name__ ==  '__main__':
    main()
