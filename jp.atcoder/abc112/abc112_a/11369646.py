import sys

*command, = map(int, sys.stdin.read().split())
n = command[0]

def main():
    if n == 1:
        print('Hello World')
    elif n == 2:
        a = command[1]; b = command[2]
        print(a + b)

if __name__ ==  '__main__':
    main()
