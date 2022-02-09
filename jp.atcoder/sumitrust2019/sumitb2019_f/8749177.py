import sys
def main():
    t1, t2, a1, a2, b1, b2 = map(int, sys.stdin.read().split())
    A1 = t1 * a1
    A2 = t2 * a2
    B1 = t1 * b1
    B2 = t2 * b2

    d = abs(A1 + A2 - B1 - B2)
    if A1 == B1:
        ans = 0
    elif A1 > B1:
        if A1 + A2 > B1 + B2:
            ans = 0
        elif A1 + A2 == B1 + B2:
            ans = 'infinity'
        else:
            ans = (A1 - B1) // d * 2 + 1


    elif A1 < B1:
        if A1 + A2 < B1 + B2:
            ans = 0
        elif A1 + A2 == B1 + B2:
            ans = 'infinity'
        else:
            ans = (B1 - A1) // d * 2 + 1

    print(ans)

if __name__ == '__main__':
    main()
