import sys

score = map(int, sys.stdin.read().split())

def main():
    rank = sorted(enumerate(score, 1), reverse=True, key=lambda x: x[1])
    for i in range(3):
        yield rank[i][0]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
