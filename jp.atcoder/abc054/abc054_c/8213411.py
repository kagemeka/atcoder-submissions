n, m = [int(x) for x in input().split()]
edges = [[int(x) for x in input().split()] for _ in range(m)]

if m < n -1:
    print(0)
    exit()

paths = []
start = 1

still_possible = True
while still_possible:
    passed = [1]
    current = start
    for i in range(1, n):
        for e in edges:
            if e[0] == current and e[1] != current and not (e[1] in passed):
                for path in paths:
                    if path[i] == e[1]:
                        break
                else:
                    passed.append(e[1])
                    current = e[1]
                    break
            elif e[0] != current and e[1] == current and not (e[0] in passed):
                for path in paths:
                    if path[i] == e[0]:
                        break
                else:
                    passed.append(e[0])
                    current = e[0]
                    break
        else: # if e all in edges are not accepted
            if passed == [1]:
                still_possible = False
            break

    if len(passed) == n:
        paths.append(passed)

print(len(paths))
