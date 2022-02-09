import sys
from string import ascii_uppercase

uppercase = set(ascii_uppercase)

s = sys.stdin.readline().rstrip()

def main():
    l = None
    words = []
    for i in range(len(s)):
        if s[i] in uppercase:
            if l is None:
                l = i
            else:
                r = i
                words.append(s[l:r+1])
                l = None

    res = ''.join(sorted(words))
    return res

if __name__ == "__main__":
    ans = main()
    print(ans)
