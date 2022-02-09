import sys

n, *b = map(int, sys.stdin.read().split())
graph = [[] for _ in range(n)]
for i in range(1, n):
    graph[b[i-1]-1].append(i)

def salary(x):
    if not graph[x]: return 1
    salaries = [salary(y) for y in graph[x]]
    salaries.sort()
    return salaries[0] + salaries[-1] + 1

def main():
    print(salary(0))

if __name__ ==  '__main__':
    main()
