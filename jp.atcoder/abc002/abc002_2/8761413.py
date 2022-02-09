import sys
ng = set('aiueo')
def main():
    w = sys.stdin.readline().rstrip()
    t = ''
    for c in w:
        if not c in ng:
            t += c
    print(t)

if __name__ == '__main__':
    main()
