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

    let a: [[Int]] = sc.intMatrix(height: h, width: w)

    var cache: [Int: Int] = [:]

    func onBoard(i: Int, j: Int) -> Bool {
        return 0 <= i && i < h && 0 <= j && j < w
    }

    let dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    func count(i: Int, j: Int) -> Int {
        if !onBoard(i: i, j: j) {
            return 0
        }
        let key = i * w + j
        if let c = cache[key] {
            return c
        }
        cache[key] = 1
        for (dy, dx) in dyx {
            let ny = i + dy
            let nx = j + dx
            if !onBoard(i: ny, j: nx) || a[ny][nx] >= a[i][j] {
                continue
            }
            cache[key]! += count(i: ny, j: nx)
        }
        return cache[key]!
    }
    print(
        (0..<h).map {
            (i) -> Int in
            (0..<w).map { (j) -> Int in count(i: i, j: j) }.reduce(0, +)
        }.reduce(0, +)
    )

}
