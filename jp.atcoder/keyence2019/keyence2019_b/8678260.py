# 2019-11-28 00:55:58(JST)
import sys
def main():
    s = sys.stdin.readline().rstrip()

    target = 'keyence'
    i = 0
    t = target[0]
    for char in s:
        if char == t:
            i += 1
            if i == 7:
                ans = 'YES'
                break
            t = target[i]
    else:
        ans = 'NO'

    print(ans)

if __name__ == '__main__':
    main()
