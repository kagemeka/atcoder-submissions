import sys

weather = 'Sunny, Cloudy, Rainy, Sunny'.split(', ')
nex = dict(zip(weather[:-1], weather[1:]))

s = sys.stdin.readline().rstrip()

def main():
    print(nex[s])

if __name__ ==  '__main__':
    main()
