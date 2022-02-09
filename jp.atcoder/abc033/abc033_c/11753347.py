import sys

s = sys.stdin.readline().rstrip()

def main():
    res = 0
    for f in s.split('+'):
        if not '0' in f: res += 1
    print(res)

if __name__ ==  '__main__':
    main()
