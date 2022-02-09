import sys

*s, = sys.stdin.readline().split()

def main():
    t = ''
    for x in s:
        t += x[0].upper()
    print(t)

if __name__ ==  '__main__':
    main()
