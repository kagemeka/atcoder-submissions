def main() -> None:
    n, x = map(int, input().split())
    s = input()

    # sousai

    # LRLRLUUUU -> L

    st = []
    for c in s:
        if c != "U":
            st.append(c)
        else:
            if st and st[-1] != "U":
                st.pop()
            else:
                st.append(c)

    # UUUULRLRLRRRL
    for c in st:
        if c == "U":
            x >>= 1
        elif c == "R":
            x = x << 1 | 1
        else:
            x = x << 1
    print(x)


if __name__ == "__main__":
    main()
