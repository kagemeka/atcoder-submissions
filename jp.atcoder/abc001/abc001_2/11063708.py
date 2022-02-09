import sys

m = int(sys.stdin.readline().rstrip())
m = m / 1000

def main():
    if m < 0.1:
        ans = '00'
    elif m <= 5:
        ans = int(m * 10)
        ans = '0' + str(ans) if ans < 10 else str(ans)
    elif m <= 30:
        ans = int(m) + 50
    elif m <= 70:
        ans = (m - 30) / 5 + 80
        ans = int(ans)
    else:
        ans = 89
    return ans

if __name__ == "__main__":
    ans = main()
    print(ans)
