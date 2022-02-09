import sys


def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    left, right = 0, 0
    for char in s:
        if char == '(':
            # if left:
            #     left -= 1
            # else:
                right += 1
        elif char == ')':
            if right:
                right -= 1
            else:
                left += 1

    ans = '(' * left + s + ')' * right
    print(ans)



if __name__ == "__main__":
    main()
