import sys

n = sys.stdin.readline().rstrip()

def main(n):
    n = n.replace('1', '0').replace('9', '1').replace('0', '9')
    print(n)

if __name__ ==  '__main__':
    main(n)
