import sys


n, *s = sys.stdin.read().split()
def main():
    print(len(set(s)))

if __name__ == '__main__':
    main()
