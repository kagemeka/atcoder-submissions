import sys

k, s = sys.stdin.read().split()
k = int(k)
def main():
    if len(s) <= k:
        print(s)
    else:
        print(s[:k] + '...')

if __name__ == '__main__':
    main()
