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

    let inf = 1 << 60
    var dist = [[Int]](repeating: [Int](repeating: inf, count: n), count: n)
    for i in 0..<n {
        dist[i][i] = 0
    }
    for _ in 0..<m {
        let a = sc.int() - 1
        let b = sc.int() - 1
        let t = sc.int()
        dist[a][b] = t
        dist[b][a] = t

    }
    for k in 0..<n {
        for i in 0..<n {
            for j in 0..<n {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
            }
        }
    }
    print(dist.map { $0.max()! }.min()!)
}
