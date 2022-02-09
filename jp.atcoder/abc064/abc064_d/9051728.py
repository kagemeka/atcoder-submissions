import sys

n = int(sys.stdin.readline().rstrip())
s = sys.stdin.readline().rstrip()

def main():
    l = r = 0
    for char in s:
        if char == '(':
            r += 1
        elif char == ')':
            if r:
                r -= 1
            else:
                l += 1

    return '(' * l + s + ')' * r

if __name__ == '__main__':
    ans = main()
    print(ans)
