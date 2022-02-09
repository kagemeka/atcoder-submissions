import typing


def main() -> typing.NoReturn:
    n = int(input())
    red = []
    blue = []
    green = []
    for _ in range(n * 2):
        a, c = input().split()
        a = int(a)
        if c == 'R':
            red.append(a)
        elif c == 'G':
            green.append(a)
        else:
            blue.append(a)

    if len(red) % 2 == 0 and len(blue) % 2 == 0:
        print(0)
        return

    if len(red) % 2 == 1:
        if len(blue) % 2 == 0:
            red, blue = blue, red
        else:
            red, green = green, red

    # red: even, blue: odd, green: odd
    # red-blue, red-green or blue-green
    red.sort()
    blue.sort()
    green.sort()
    # pattern blue-green
    inf = 1 << 60
    res = inf
    i = 0
    for x in blue:
        while green[i] < x and i + 1 < len(green):
            res = min(res, abs(x - green[i]))
            i += 1
        res = min(res, abs(x - green[i]))
    if len(red) == 0:
        print(res)
        return

    blue_min = [0] * len(red)
    green_min = [0] * len(red)
    i = 0
    for j, x in enumerate(red):
        while blue[i] < x and i + 1 < len(blue):
            blue_min[j] = min(blue_min[j], abs(x - blue[i]))
            i += 1
        blue_min[j] = min(blue_min[j], abs(x - blue[i]))

    i = 0
    for j, x in enumerate(red):
        while green[i] < x and i + 1 < len(green):
            green_min[j] = min(green_min[j], abs(x - green[i]))
            i += 1
        green_min[j] = min(green_min[j], abs(x - green[i]))

    arg_blue = sorted(range(len(red)), key=lambda i: blue_min[i])
    arg_green = sorted(range(len(red)), key=lambda i: green_min[i])
    if arg_green[0] != arg_blue[0]:
        res = min(res, blue_min[arg_blue[0]] + green_min[arg_green[0]])
    else:
        res = min(
            res,
            blue_min[arg_blue[0]] + green_min[arg_green[1]],
            blue_min[arg_blue[1]] + green_min[arg_green[0]],
        )
    print(res)



main()
