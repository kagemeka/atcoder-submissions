import sys

a = set(map(int, sys.stdin.read().split()))

def main():
    for i in range(1, 4):
        if not i in a:
            print(i)
            return

if __name__ ==  '__main__':
    main()
