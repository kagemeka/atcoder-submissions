from __future__ import annotations


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    st = []
    cnt = 0
    for x in a:
        if st and st[-1] != x:
            cnt = 0
        st.append(x)
        cnt += 1
        if x == cnt:
            while cnt:
                st.pop()
                cnt -= 1
        print(len(st))
    # print(len(st))


if __name__ == "__main__":
    main()
