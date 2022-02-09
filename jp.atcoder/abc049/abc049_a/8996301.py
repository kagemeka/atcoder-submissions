import sys

vowels = set('aeiou')
c = sys.stdin.readline().rstrip()

def main():
    if c in vowels:
        return 'vowel'
    return 'consonant'

if __name__ == '__main__':
    ans = main()
    print(ans)
