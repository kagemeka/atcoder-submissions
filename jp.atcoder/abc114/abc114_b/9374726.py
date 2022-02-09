import sys

target = 753

s = sys.stdin.readline().rstrip()

def main():
    d = 642
    for i in range(len(s) - 2):
        d = min(d, abs(target - int(s[i:i+3])))

    return d

if __name__ == '__main__':
    ans = main()
    print(ans)
