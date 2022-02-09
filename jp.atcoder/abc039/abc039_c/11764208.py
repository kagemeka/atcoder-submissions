import sys
keyboard = 'WBWBWWBWBWBW' * 3
res = 'Do, , Re, , Mi, Fa, , So, , La, , Si'.split(', ')
s = sys.stdin.readline().rstrip()

def main():
    print(res[keyboard.find(s)])

if __name__ ==  '__main__':
    main()
