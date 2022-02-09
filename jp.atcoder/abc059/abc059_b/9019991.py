import sys

a, b = sys.stdin.read().split()

def main():
    la = len(a)
    lb = len(b)
    if la > lb:
        return 'GREATER'
    elif la < lb:
        return 'LESS'
    else:
        for i in range(la):
            if a[i] > b[i]:
                return 'GREATER'
            elif a[i] < b[i]:
                return 'LESS'
        return 'EQUAL'

if __name__ == '__main__':
    ans = main()
    print(ans)
