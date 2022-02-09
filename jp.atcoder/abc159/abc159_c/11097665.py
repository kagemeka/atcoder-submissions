import sys

l = int(sys.stdin.readline().rstrip())

def main():
    return pow(l/3, 3)

if __name__ == "__main__":
    ans = main()
    print(ans)
