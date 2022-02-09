import sys

c = sys.stdin.readline().rstrip()

def main():
    return chr(ord(c) + 1)

if __name__ == '__main__':
    ans = main()
    print(ans)
