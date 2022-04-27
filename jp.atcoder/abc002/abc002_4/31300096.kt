private fun readString() = readLine()!!

private fun readStrings() = readString().split(" ")

private fun readInt() = readString().toInt()

private fun readInts() = readStrings().map { it.toInt() }

fun main() {
    var (n, m) = readInts()
    var relations: MutableList<Int> = (0..n - 1).map { 1.shl(it) }.toMutableList()

    for (i in 0 until m) {
        var (x: Int, y: Int) = readInts()
        --x
        --y
        relations[x] = relations[x] or 1.shl(y)
        relations[y] = relations[y] or 1.shl(x)
    }

    var mx = 0
    for (s in 0 until 1.shl(n)) {
        var t = s
        var count = 0
        for (i in 0 until n) {
            if ((s.shr(i) and 1) == 0) {
                continue
            }
            t = t and relations[i]
            count += 1
        }
        if (t == s) {
            mx = maxOf(mx, count)
        }
    }

    println(mx)
}
