def main() -> None:
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    def calc(x0, y0, x1, y1, x2, y2):
        if y2 == y0:
            print(x2, y1)
        else:
            print(x2, y0)

    if x0 == x1:
        calc(x0, y0, x1, y1, x2, y2)
    elif x1 == x2:
        calc(x1, y1, x2, y2, x0, y0)
    else:
        calc(x2, y2, x0, y0, x1, y1)

        # if y0 == y1:



if __name__ == "__main__":
    main()
