import sys

def main():
    n = sys.stdin.readline().rstrip()

    cnt = 1
    for i in range(3):
        if n[i] == n[i+1]:
            cnt += 1
            if cnt == 3:
                ans = 'Yes'
                break
        else:
            cnt = 0
    else:
        ans = 'No'

    print(ans)

if __name__ == "__main__":
    main()
