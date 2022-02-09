import sys

vowels = set('aeiuo')

c = sys.stdin.readline().rstrip()

def main():
    ans = 'vowel' if c in vowels else 'consonant'
    print(ans)

if __name__ ==  '__main__':
    main()
