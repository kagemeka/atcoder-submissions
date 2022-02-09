import sys

a = sys.stdin.readline().split()

def main():
    a.sort(reverse=True)
    a.insert(2, '+')
    return eval(''.join(a))

if __name__ == '__main__':
    ans = main()
    print(ans)
