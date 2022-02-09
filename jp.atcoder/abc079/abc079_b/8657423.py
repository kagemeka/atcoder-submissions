import sys

lucas_nums = [None] * 100
lucas_nums[0], lucas_nums[1] = 2, 1
for i in range(2, 100):
    lucas_nums[i] = lucas_nums[i-2] + lucas_nums[i-1]

def main():
    n = int(sys.stdin.readline().rstrip())
    print(lucas_nums[n])

if __name__ == "__main__":
    main()
