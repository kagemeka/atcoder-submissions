import sys

a = 'ATCG'
b = 'TAGC'
bond = dict(zip(a, b))

print(bond)
def main():
    b = sys.stdin.readline().rstrip()
    print(bond[b])

if __name__ == "__main__":
    main()
