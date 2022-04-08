def main() -> None:
    s = "DiscoPresentsDiscoveryChannelProgrammingContest2016"
    n = int(input())
    i = 0
    while i < 51:
        print(s[i : i + n])
        i += n

if __name__ == "__main__":
    main()
