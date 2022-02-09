import sys

commands = sys.stdin.readline().rstrip()

def main():
    res = []
    for c in commands:
        if c == 'B':
            if res:
                res.pop()
        else:
            res.append(c)
    return ''.join(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
