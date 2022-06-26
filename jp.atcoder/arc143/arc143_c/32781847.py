# / mypy: ignore-errors
import typing


def main() -> None:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    win_count = 0
    draw_and_win_count = 0
    for c in a:
        draw_and_win = False
        if c >= x:
            r = (c - x) % (x + y)
            # if r < min(x, y) or x <= r < y:
            if r < y:
                draw_and_win = True
        win = draw_and_win
        r = c % (x + y)
        win |= r < y
        win_count += win
        draw_and_win_count += draw_and_win
    if win_count != n or draw_and_win_count == 0:
        print("Second")
    else:
        print("First")


main()
