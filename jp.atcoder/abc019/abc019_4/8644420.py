# 2019-11-25 12:34:24(JST)
import sys
def main():
    n = int(sys.stdin.readline().rstrip())

    # root = 1 とする
    diameter = 0
    for i in range(2, n+1):
        # print(f'? 1 {i}')
        # f-string は ver.3.6から
        print('? {0} {1}'.format(1, i))
        sys.stdout.flush
        dist = int(sys.stdin.readline().rstrip())
        if dist > diameter:
            v, diameter = i, dist

    for i in range(2, n+1):
        if i != v:
            # print(f'? {v} {i}')
            print('? {0} {1}'.format(v, i))
            sys.stdout.flush
            dist = int(sys.stdin.readline().rstrip())
            diameter = max(diameter, dist)

    print(f'! {diameter}')

if __name__ == '__main__':
    main()
