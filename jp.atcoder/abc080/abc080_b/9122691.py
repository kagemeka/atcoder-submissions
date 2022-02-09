import sys

def is_harshad_number(x):
    return not x % sum(list(map(int, list(str(n)))))

n = int(sys.stdin.readline().rstrip())

def main():
    return 'Yes' if is_harshad_number(n) else 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
