import sys

a, b = map(int, sys.stdin.readline().split())

def main():
    flag = False
    if not a % 3: flag = True
    elif not b % 3: flag = True
    elif not (a + b) % 3: flag = True
    ans = 'Possible' if flag else 'Impossible'
    print(ans)

if __name__ ==  '__main__':
    main()
