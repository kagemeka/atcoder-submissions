import sys

y, m, d = sys.stdin.readline().rstrip().split('/')
y = '2018'

def main():
    print('/'.join([y, m, d]))

if __name__ ==  '__main__':
    main()
