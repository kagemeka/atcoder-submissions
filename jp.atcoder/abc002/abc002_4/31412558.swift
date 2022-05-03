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

    func string() -> String {
        while tokens.isEmpty {
            tokens = readStrings().reversed()
        }
        return tokens.popLast()!
    }

    func int() -> Int {
        return Int(string())!
    }

}

func main() {
    let sc = Scanner()
    let n = sc.int()
    let m = sc.int()

    var relations = (0..<n).map { 1 << $0 }
    for _ in 0..<m {
        let x = sc.int() - 1
        let y = sc.int() - 1
        relations[x] |= 1 << y
        relations[y] |= 1 << x
    }

    var mx = 0
    for s in 0..<1 << n {
        var t = s
        var count = 0
        for i in 0..<n {
            if ~s >> i & 1 == 1 {
                continue
            }
            count += 1
            t &= relations[i]
        }
        if t != s {
            continue
        }
        mx = max(mx, count)
    }
    print(mx)

}
