private fun readString() = readLine()!!

private fun readStrings() = readString().split(" ")

private fun readInt() = readString().toInt()

private fun readInts() = readStrings().map { it.toInt() }

fun main() {
    val (n, m) = readInts()

    val INF = 1.shl(29)

    var g = Array<Array<Int>>(n) { Array(n) { INF } }

    for (i in 0 until m) {
        var (a, b, t) = readInts()
        --a
        --b
        g[a][b] = t
        g[b][a] = t
    }
    for (i in 0..n - 1) {
        g[i][i] = 0
    }

    for (k in 0 until n) {
        for (i in 0..n - 1) {
            for (j in 0..n - 1) {
                g[i][j] = minOf(g[i][j], g[i][k] + g[k][j])
            }
        }
    }

  	println(g.map { it.max()!! }.min())

}
