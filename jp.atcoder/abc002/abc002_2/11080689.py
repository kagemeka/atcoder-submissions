import sys

vowels = set('aeiuo')

w = sys.stdin.readline().rstrip()

def main():
    s = ''
    for c in w:
        if not c in vowels:
            s += c

    return s

if __name__ == '__main__':
    ans = main()
    print(ans)
