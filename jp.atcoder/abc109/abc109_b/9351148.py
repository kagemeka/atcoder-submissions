import sys

n, *words = sys.stdin.read().split()
n = int(n)

def main():
    announced = set()
    last = words[0][0]
    for w in words:
        if w in announced:
            return 'No'
        elif w[0] != last:
            return 'No'
        announced.add(w)
        last = w[-1]
    return 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)
