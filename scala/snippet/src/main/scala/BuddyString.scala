package main.scala

object BuddyString extends App {
  def isBuddyString(a: String, b: String): Boolean = (a, b) match {
    case _ if a.length() != b.length()                     => false
    case _ if a.length() == 2 && b.length() == 2 && a == b => true
    case _ if a.toSet != b.toSet                           => false
    case _ if a == b                                       => false
    case (a, b ) => {
        val diff = diffString(a.toList, b.toList, List.empty[Int])
        diff.count( a => a == 1) == 2
    }

  }

  def diffString(a: List[Char], b: List[Char], acc: List[Int]): List[Int] =
    (a, b) match {
      case (Nil, Nil) => acc
      case ((xa :: xs), (yb :: ys)) if xa == yb => diffString(xs, ys, acc ++ List(0))
      case ((xa :: xs), (yb :: ys)) => diffString(xs, ys, acc ++ List(1))
    }


    println(isBuddyString("aaacb", "aaabcz"))
}
