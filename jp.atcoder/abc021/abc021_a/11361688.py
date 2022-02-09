import sys

n = int(sys.stdin.readline().rstrip())

def main():
    res = [pow(2, i) for i in range(4) if n >> i & 1]
    print(len(res))
    print(*res, sep='\n')

if __name__ ==  '__main__':
    main()
