import sys

bond = dict(zip('ATCG', 'TAGC'))

def main():
    b = sys.stdin.readline().rstrip()
    print(bond[b])

if __name__ == "__main__":
    main()
