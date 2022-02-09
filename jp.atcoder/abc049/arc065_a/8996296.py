import sys

s = sys.stdin.readline().rstrip()

def main():
    t = s
    cands = 'eraser, erase, dreamer, dream'.split(', ')
    for c in cands:
        t = t.replace(c, '')

    return 'YES' if not t else 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
