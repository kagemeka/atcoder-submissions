import sys

corresponding = dict(zip('ACGT', 'TGCA'))

b = sys.stdin.readline().rstrip()

def main():
    return corresponding[b]

if __name__ == '__main__':
    ans = main()
    print(ans)
