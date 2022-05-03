main()

private func readStrings() -> [String] {
    return readLine()!.split(separator: " ").map { String($0) }
}

private func readInts() -> [Int] {
    return readLine()!.split(separator: " ").map { Int($0)! }
}

private class Scanner {
    private var tokens: [String] = []

    init() {}

    func next() -> String {
        while tokens.isEmpty {
            tokens = readStrings().reversed()
        }
        return tokens.popLast()!
    }

    func nextInt() -> Int {
        return Int(next())!
    }

}

func main() {
    let sc = Scanner()
    print(sc.nextInt() - sc.nextInt())
}
