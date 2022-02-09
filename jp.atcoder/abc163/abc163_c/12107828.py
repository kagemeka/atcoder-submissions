import sys

n, *a = map(int, sys.stdin.read().split())
graph = [[] for _ in range(n)]
for i in range(n - 1):
    graph[a[i]-1].append(i)
def main():
    for i in range(n):
        print(len(graph[i]))


if __name__ == '__main__':
    main()
