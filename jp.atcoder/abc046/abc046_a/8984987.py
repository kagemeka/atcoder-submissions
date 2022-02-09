import sys

paints = sys.stdin.readline().split()

def main():
    ans = len(set(paints))
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
