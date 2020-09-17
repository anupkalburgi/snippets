package snippet

object ADWH_1_1_6 extends App {
// foldright has a very different behaviour in haskell and scala
// in scala foldRight never terminates early, as it is implemented using a while, and does take O(n)
// but takeWhile, does break out eaarly because the loop test fails


  def op(x: Int, xs: List[Int]): List[Int] = {
    if (x % 2 == 0) x :: xs
    else List.empty[Int]
  }

  val llss =
    List(2, 3, 4, 5).foldRight(List.empty[Int])((x: Int, xs: List[Int]) => {
      print(s"yes $x");
      if (x % 2 == 0) { x :: xs }
      else List.empty[Int]
    })
  println(llss)

}
