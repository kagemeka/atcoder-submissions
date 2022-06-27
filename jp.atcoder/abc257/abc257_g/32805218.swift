import Foundation

private func readStrings() -> [String] {
  return readLine()!.split(separator: " ").map { String($0) }
}
private class Scanner {
  private var tokens: [String] = []
  init() {}
  func str() -> String {
    while tokens.isEmpty { tokens = readStrings().reversed() }
    return tokens.popLast()!
  }
  func strs(_ n: Int) -> [String] { return (0..<n).map { _ in str() } }
  func int() -> Int { return Int(str())! }
  func ints(_ n: Int) -> [Int] { return (0..<n).map { _ in int() } }
  func intMatrix(_ h: Int, _ w: Int) -> [[Int]] {
    return (0..<h).map { _ in (0..<w).map { _ in int() } }
  }
}

private func printArr<T>(_ a: [T]) {
  let n = a.count
  for i in 0..<n { print(a[i], terminator: i == n - 1 ? "\n" : " ") }
}

func morrisPrattTable<T: Comparable>(_ a: [T]) -> [Int] {
  let n = a.count
  var lb = [Int](repeating: 0, count: n)
  var d = 0
  for i in 1..<n {
    while d != 0 && a[d] != a[i] { d = lb[d - 1] }
    if a[d] == a[i] { d += 1 }
    lb[i] = d
  }
  return lb
}

func main() {
  let sc = Scanner()
  let s = sc.str()
  let t = sc.str()
  let (n, m) = (s.count, t.count)
  let lb = Array(morrisPrattTable(Array(s + "$" + t))[(n + 1)...])
  var k = 0
  var i = m
  while i > 0 {
    let d = lb[i - 1]
    if d == 0 {
      print(-1)
      return
    }
    i -= d
    k += 1
  }
  print(k)
}

main()
