def main() -> None:
    digits = list(map(int, input()))

    for sign_bits in range(1 << 3):
        v = digits[0]
        s = str(v)
        for i in range(3):
            if sign_bits >> i & 1:
                v += digits[i + 1]
                s += "+" + str(digits[i + 1])
            else:
                v -= digits[i + 1]
                s += "-" + str(digits[i + 1])
        if v == 7:
            print(f"{s}=7")
            return


if __name__ == "__main__":
    main()
