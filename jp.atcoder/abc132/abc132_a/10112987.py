import sys

s = sys.stdin.readline().rstrip()

def main():
    for char in set(s):
        if s.count(char) != 2:
            return 'No'
    return 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)
