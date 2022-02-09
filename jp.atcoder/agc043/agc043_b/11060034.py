import sys
import random

n = int(sys.stdin.readline().rstrip())
*s, = map(int, list(sys.stdin.readline().rstrip()))

def main():
    return random.randrange(3)

if __name__ == "__main__":
    ans = main()
    print(ans)
