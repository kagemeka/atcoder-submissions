import sys

n, *operations = sys.stdin.read().split()

def main():
    u, f, r = 1, 2, 3
    tot = 1
    for o in operations:
        if o == 'East':
            u, r = 7 - r, u
        elif o == 'Left':
            f, r = 7 - r, f
        elif o == 'North':
            f, u = 7 - u, f
        elif o == 'Right':
            r, f = 7 - f, r
        elif o == 'South':
            u, f = 7 - f, u
        elif o == 'West':
            r, u = 7 - u, r
        tot += u
    return tot

if __name__ == "__main__":
    ans = main()
    print(ans)
