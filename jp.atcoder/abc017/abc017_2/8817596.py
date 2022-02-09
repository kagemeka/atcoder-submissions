import sys

x = sys.stdin.readline().rstrip()
tail = set('ch, o, k, u'.split(', '))
l = len(x)

def main():
    i = 0
    while i < l:
        if x[i:i+2] == 'ch':
            i += 2
        elif x[i] in tail:
            i += 1
        else:
            break
    else:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
