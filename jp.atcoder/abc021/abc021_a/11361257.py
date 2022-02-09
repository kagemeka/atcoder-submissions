import sys

n = int(sys.stdin.readline().rstrip())

def main():
    for i in range(4):
        if n >> i & 1:
            print(pow(2, i))

if __name__ ==  '__main__':
    main()
