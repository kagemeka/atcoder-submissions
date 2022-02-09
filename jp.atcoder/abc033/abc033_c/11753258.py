import sys

s = sys.stdin.readline().rstrip()

def main():
    a = [eval(f) for f in s.split('+')]
    print(len(a) - a.count(0))

if __name__ ==  '__main__':
    main()
