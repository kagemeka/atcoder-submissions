private func readStrings() -> [String] {
    return readLine()!.split(separator: " ").map { String($0) }
}

private func readInts() -> [Int] {
    return readLine()!.split(separator: " ").map { Int($0)! }
}

func main() {
    let h1 = Int(readLine()!)!
    let h2 = Int(readLine()!)!
    print(h1 - h2)

}

main()
