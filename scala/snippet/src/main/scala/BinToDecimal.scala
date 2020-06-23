package snippet


object BinToDecimal extends App {
    // Accepts already revresed BinList
    // multiplier starts  with 1
    // sum starts with 0
    def binToDecimal(bin: List[Int], multiplier: Int, sum: Int): Int = bin match {
        case Nil => sum
        case head :: tl => 
        binToDecimal(tl, multiplier * 2, sum + (head * multiplier))
    }

    val input = List(1, 1, 0, 0, 0, 0, 0, 1)
    val expected = 193
    val actual = binToDecimal(input.reverse, 1, 0)
    println(actual)
    assert(expected == actual)
}