def main() -> None:
    n = int(input())
    st = set()
    for _ in range(n):
        l, *a = map(int, input().split())
        st.add(tuple(a))
    print(len(st))


if __name__ == "__main__":
    main()
