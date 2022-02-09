import sys

bond = dict(('A', 'T'), ('T', 'A',), ('C', 'G'), ('G', 'C'))

def main():
    b = sys.stdin.readline().rstrip()
    print(bond[b])

if __name__ == "__main__":
    main()
