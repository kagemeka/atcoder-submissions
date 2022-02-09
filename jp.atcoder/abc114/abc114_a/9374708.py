import sys

cand = [7, 5, 3]

x = int(sys.stdin.readline().rstrip())

def main():
    return 'YES' if x in cand else 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
