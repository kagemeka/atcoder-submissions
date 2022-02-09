import sys

n = int(sys.stdin.readline().rstrip())

def hms(h, m, s):
    t = [h, m, s]
    for i in range(3):
        if t[i] < 10:
            t[i] = '0' + str(t[i])
        else:
            t[i] = str(t[i])
    return ':'.join(t)

def main():

    h, r = divmod(n, 60 ** 2)
    if h >= 24:
        return hms(23, 59, 59)

    m, s = divmod(r, 60)
    return hms(h, m, s)

if __name__ == '__main__':
    print(main())
