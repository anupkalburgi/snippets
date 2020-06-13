package snippet

object BinaryAdd extends App {
  println("So that is the diff")
  val ll = List(1,0,0,1,1)
  val rr = List(1,1,1,0,1)
  println(addBinary(ll.reverse, rr.reverse, 0, List.empty[Int]))
  // Find out how zipAll works

  def addBinary(
      l: List[Int],
      r: List[Int],
      carry: Int,
      ans: List[Int]
  ): List[Int] = {
    (l, r, carry) match {
      case (Nil, Nil , _) => carry :: ans
      case (lh :: lt, Nil, c) => l ++ ans // I have to add c to lh
      case (Nil, rh :: rt, c) => r ++ ans // I have to add c to lh
      case (lh :: lt, rh :: rt, c) =>
        val (c1, n1) = addBin(lh, rh, c)
        addBinary(lt, rt, c1, n1 :: ans)
      // case _ => throw IllegalArgumentException("not this please")
    }
  }

  def addBin(a: Int, b: Int, carry: Int): (Int, Int) = {
    (a, b, carry) match {
      case (0, 0, 0) => (0, 0)
      case (0, 0, 1) => (0, 1)
      case (0, 1, 0) => (0, 1)
      case (0, 1, 1) => (1, 0)
      case (1, 0, 0) => (0, 1)
      case (1, 0, 1) => (1, 0)
      case (1, 1, 0) => (1, 0)
      case (1, 1, 1) => (1, 1)
      // case _ => new IllegalArgumentException
    }
    // }

  }
}
