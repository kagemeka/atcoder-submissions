import sys

*candies, = map(int, sys.stdin.readline().split())

def main():
    candies.sort()
    if candies[0] + candies[1] == candies[2]:
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    ans = main()
    print(ans)
