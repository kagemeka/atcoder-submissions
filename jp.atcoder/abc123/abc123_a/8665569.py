import sys

def main():
    *antennas, k = map(int, sys.stdin.read().split())
    if antennas[-1] - antennas[0] > k:
            print(':(')
            sys.exit()
    print('Yay!')

if __name__ == "__main__":
    main()
