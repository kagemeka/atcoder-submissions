import sys

s = sys.stdin.readline().split()

def main():
    t = ''.join([x[0].upper() for x in s])
    print(t)

if __name__ ==  '__main__':
    main()
