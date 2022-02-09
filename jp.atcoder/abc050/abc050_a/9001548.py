import sys

formula = sys.stdin.readline().rstrip()

def main():
    return eval(formula)

if __name__ == '__main__':
    ans = main()
    print(ans)
