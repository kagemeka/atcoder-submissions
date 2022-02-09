import sys

sign = '+-'

def main():
    a, b, c, d = list(sys.stdin.readline().rstrip())

    for i in sign:
        for j in sign:
            for k in sign:
                left = a + i + b + j + c + k + d
                if eval(left) == 7:
                    print(left+'=7')
                    sys.exit()

if __name__ == "__main__":
    main()
