import sys

s = sys.stdin.readline().rstrip()

def main():
    try:
        n = int(s)
    except:
        return 'error'

    return n * 2

if __name__ == "__main__":
    ans = main()
    print(ans)
