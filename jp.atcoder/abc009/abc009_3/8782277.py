import sys

n, k = map(int, sys.stdin.readline().split())
s = [ord(c) - 97 for c in sys.stdin.readline().rstrip()]

def swap(i, j):
    s[i], s[j] = s[j], s[i]

def main():
    r = k
    changed = [False] * n

    for i in range(n-1):
        cand = sorted(x for x in set(s[i+1:]) if x < s[i])
        if not cand:
            continue
        swapped = False
        for c in cand:
            for j in range(n-1, i, -1):
            # for j in range(i + 1, n):
                if s[j] == c:
                    cnt = changed[i] + changed[j]
                    if cnt == 2:
                        swap(i, j)
                        swapped = True
                        break
                    elif cnt == 1:
                        if r >= 1:
                            swap(i, j)
                            r -= 1
                            changed[i], changed[j] = True, True
                            swapped = True
                            break
                    elif cnt == 0:
                        if r >= 2:
                            swap(i, j)
                            r -= 2
                            changed[i], changed[j] = True, True
                            swapped = True
                            break

            if swapped:
                break

    ans = ''.join([chr(o + 97) for o in s])
    print(ans)

if __name__ == '__main__':
    main()
