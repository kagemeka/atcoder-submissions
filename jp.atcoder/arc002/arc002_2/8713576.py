import sys

def is_leap_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

less_than_31 = set([2, 4, 6, 9, 11])

def main():
    y, m, d = map(int, sys.stdin.readline().rstrip().split('/'))


    for _ in range(365):
        if y % m == 0:
            r = y // m
            if r % d == 0:
                break
            else:
                d += 1
                if m in less_than_31:
                    if m == 2:
                        if is_leap_year(y):
                            if d == 30:
                                m += 1
                                d = 1
                        else:
                            if d == 29:
                                m += 1
                                d = 1
                    else:
                        if d == 31:
                            m += 1
                            d = 1
                else:
                    if d == 32:
                        if m == 12:
                            y += 1
                            m = 1
                            d = 1
                            break
                        else:
                            m += 1
                            d = 1
        else:
            m += 1
            d = 1
            if m == 13:
                y += 1
                m = 1
                break

    y = str(y)
    m = '0' + str(m) if m < 10 else str(m)
    d = '0' + str(d) if d < 10 else str(d)
    print('/'.join([y, m, d]))


if __name__ == '__main__':
    main()
