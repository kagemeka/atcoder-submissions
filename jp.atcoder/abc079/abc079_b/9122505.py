import sys

lucas_nums = [None] * 101
lucas_nums[0] = 2
lucas_nums[1] = 1
for i in range(2, 101):
    lucas_nums[i] = lucas_nums[i-2] + lucas_nums[i-1]

n = int(sys.stdin.readline().rstrip())

def main():
    return lucas_nums[n]

if __name__ == '__main__':
    ans = main()
    print(ans)
