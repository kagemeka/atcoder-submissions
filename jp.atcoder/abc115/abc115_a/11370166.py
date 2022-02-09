import sys

d = int(sys.stdin.readline().rstrip())

def main():
    print('Christmas' + ' Eve' * (25 - d))

if __name__ ==  '__main__':
    main()
