import sys

n, *b = map(int, sys.stdin.read().split())

def main():
    subordinate = [[] for _ in range(n)]
    for i in range(n-1):
        subordinate[b[i]-1].append(i+1)

    rank = [[] for _ in range(n)]
    stack = [(0, 0)]
    while stack:
        boss, r = stack.pop()
        rank[r].append(boss)
        for s in subordinate[boss]:
            stack.append((s, r+1))

    sarary = [1] * n
    for r in range(n-1, -1, -1):
        for boss in rank[r]:
            if not subordinate[boss]:
                continue
            sub_sararies = []
            for s in subordinate[boss]:
                sub_sararies.append(sarary[s])
            sub_sararies.sort()
            sarary[boss] += sub_sararies[0] + sub_sararies[-1]

    return sarary[0]

if __name__ == '__main__':
    ans = main()
    print(ans)
