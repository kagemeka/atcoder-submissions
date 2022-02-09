import sys

s = sys.stdin.readline().rstrip()

def main():
    flag = s[2] == s[3] and s[4] == s[5]
    print("Yes" if flag else "No")

if __name__ == "__main__":
    main()
