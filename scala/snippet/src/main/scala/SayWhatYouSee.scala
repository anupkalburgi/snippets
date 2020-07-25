package main.scala

object SayWhatYouSee extends App {
    def say(nums: List[Int], res: List[Int]): List[Int] =
    nums match {
        case Nil => res
        case x :: xs => 
        val cntx = xs.takeWhile(l => l == x)
        val rem = xs.dropWhile(l => l == x )
        say(rem, res ++ List(cntx.length + 1, x))
    }
    // cannot do this as order is imortant, but can use something like linked hashmap
    //  {
    // val tmp = nums.groupBy(id => id)
    // }
    def look(nterm: Int): List[Int] = {
        nterm match {
            case x if x <= 1 => List(1)
            case _ => say(look(nterm-1), List.empty[Int])
        }
    }

    println(look(1))
    println(look(2))
    println(look(3))
    println(look(4))
    println(look(5))
    println(look(6))
    println(look(7))

    // sayCnt(3, List.empty[Int])
    // sayCnt(countSay(3), List.empty[Int])
  
}
