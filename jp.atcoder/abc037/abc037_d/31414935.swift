main()

private func readStrings() -> [String] {
    return readLine()!.split(separator: " ").map { String($0) }
}

private func readInts() -> [Int] {
    return readLine()!.split(separator: " ").map { Int($0)! }
}

private func readIntMatrix(height: Int) -> [[Int]] {
    return (0..<height).map { _ in readInts() }
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

    func strings(size: Int) -> [String] {
        return (0..<size).map { _ in string() }
    }

    func int() -> Int {
        return Int(string())!
    }

    func ints(size: Int) -> [Int] {
        return (0..<size).map { _ in int() }
    }

    func intMatrix(height: Int, width: Int) -> [[Int]] {
        return (0..<height).map { _ in (0..<width).map { _ in int() } }
    }

}

func main() {
    let sc = Scanner()
    let h = sc.int()
    let w = sc.int()
    let mod = 1_000_000_007
    let a: [[Int]] = sc.intMatrix(height: h, width: w)

    func onBoard(i: Int, j: Int) -> Bool {
        return 0 <= i && i < h && 0 <= j && j < w
    }

    let dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    var count = [[Int]](repeating: [Int](repeating: 1, count: w), count: h)

    var indices = (0..<h).map { (i) -> [(Int, Int)] in
        (0..<w).map { (j) -> (Int, Int) in
            return (i, j)
        }
    }.flatMap { $0 }
    indices.sort(by: { (x, y) -> Bool in
        return a[x.0][x.1] <= a[y.0][y.1]
    })
    var tot = 0
    for (i, j) in indices {
        count[i][j] %= mod
        tot += count[i][j]
        tot %= mod
        for (dy, dx) in dyx {
            let ni = i + dy
            let nj = j + dx
            if !onBoard(i: ni, j: nj) || a[ni][nj] <= a[i][j] {
                continue
            }
            count[ni][nj] += count[i][j]
        }
    }
    print(tot)

}
