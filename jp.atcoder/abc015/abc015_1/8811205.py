import sys

a, b = sys.stdin.read().split()

def main():
    return a if len(a) > len(b) else b

if __name__ == '__main__':
    ans = main()
    print(ans)
