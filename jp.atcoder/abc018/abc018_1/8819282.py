import sys

score = map(int, sys.stdin.read().split())

def main():
    rank = sorted(enumerate(score), reverse=True, key=lambda x: x[1])
    res = [None] * 3
    for i in range(3):
        res[rank[i][0]] = i + 1
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
