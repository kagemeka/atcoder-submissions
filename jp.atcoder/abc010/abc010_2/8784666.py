import sys

n, *petals = map(int, sys.stdin.read().split())

def main():

    cnt = 0
    for petal in petals:
        while (not petal & 1) or petal % 6 == 5:
            petal -= 1
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()
