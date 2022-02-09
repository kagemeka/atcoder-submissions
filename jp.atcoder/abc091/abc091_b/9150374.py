import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.read().split()

def main():

    score = defaultdict(int)
    for w in s[:n]:
        score[w] += 1
    for w in s[n+1:]:
        score[w] -= 1

    ans = max(max(score.values()), 0)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
