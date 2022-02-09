import sys

s = sys.stdin.readline().rstrip()

def main():
    if s[0] == 'A':
        if 'C' in s[2:-1]:
            cnt = 0
            for letter in s:
                if 65 <= ord(letter) <= 90:
                    cnt += 1
            if cnt == 2:
                return 'AC'
    return 'WA'

if __name__ == '__main__':
    ans = main()
    print(ans)
