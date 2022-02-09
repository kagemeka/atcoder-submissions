import sys
def main():
    n = int(sys.stdin.readline().rstrip())
    average_salary = 10000 * (1 + n) * n // 2 / n
    print(average_salary)

if __name__ == '__main__':
    main()
