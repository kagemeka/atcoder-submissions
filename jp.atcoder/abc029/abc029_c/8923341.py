import sys
from itertools import product

n = int(sys.stdin.readline().rstrip())

def main():
    ans = [''.join(chars) for chars in product('abc', repeat=n)]
    return ans

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
