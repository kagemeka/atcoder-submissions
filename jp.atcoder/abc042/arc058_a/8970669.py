import sys

n, k, *dislikes = sys.stdin.read().split()
n = int(n)
dislikes = set(dislikes)

def main():
    i = n
    while True:
        if set(str(i)) & dislikes:
            i += 1
            continue
        return i

if __name__ == '__main__':
    ans = main()
    print(ans)
