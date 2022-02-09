import sys

def is_palindrome(s):
    return s == s[::-1]

s = sys.stdin.readline().rstrip()
n = len(s)

def main():
    res = is_palindrome(s[:n//2]) and is_palindrome(s[n//2+1:])
    return 'Yes' if is_palindrome(s) and res else 'No'

if __name__ == "__main__":
    ans = main()
    print(ans)
