import sys

n = sys.stdin.readline().rstrip()

def main():
    ans = 'Yes'
    if n[1] != n[2]:
        ans = 'No'
    else:
        if n[0] != n[1] and n[2] != n[3]:
            ans = 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
