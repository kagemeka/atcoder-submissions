import sys

t = 'eraser, erase, dreamer, dream'.split(', ')
def obtainable(s):
    for x in t:
        s = s.replace(x, '')
    return not s

s = sys.stdin.readline().rstrip()

def main():
    print("YES" if obtainable(s) else "NO")

if __name__ ==  '__main__':
    main()
