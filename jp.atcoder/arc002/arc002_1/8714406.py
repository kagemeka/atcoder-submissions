import sys

def is_leap_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

def main():
    print('YES' if is_leap_year(int(sys.stdin.readline().rstrip())) else 'NO')

if __name__ == '__main__':
    main()
