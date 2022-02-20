# from __future__ import annotations


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    st = [-1]
    counts = [1]
    cnt = 0
    for x in a:
        if st and st[-1] != x:
            counts.append(1)
        else:
            counts[-1] += 1
        st.append(x)
        # cnt += 1
        if x == counts[-1]:
            while counts[-1]:
                st.pop()
                counts[-1] -= 1
            counts.pop()
        print(len(st) - 1)
    # print(len(st))


if __name__ == "__main__":
    main()
