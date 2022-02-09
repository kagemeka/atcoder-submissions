import sys

keyboard = 'WBWBWWBWBWBW' * 3

s = sys.stdin.readline().rstrip()

def main():
    res = 'Do, Re, Mi, Fa, So, La, Si'.split(', ')
    ans = res[keyboard.index(s)]
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
