package snippet.parsenumber

object ValidNumberV1 extends App {

  def isNumber(s: String): Boolean = {
    numbers.runP(s.toList) match {
      case Nil => false
      case cs   => println(cs)
      true
    }
  }

  case class Parser[+A](runP: List[Char] => List[(A, List[Char])]) {
    def map[B](f: A => B): Parser[B] = 
        Parser{ l => runP(l) match {
            case Nil => Nil
            case xs => xs.map(x => (f(x._1), x._2) )
        }}
    def flatMap[B](f: A => Parser[B]): Parser[B] = 
        Parser(l =>
        runP(l) match {
            case Nil => Nil
            case xs => xs.flatMap(x => ( f(x._1).runP(x._2) ) )
            }
        )
  }

  val fail = Parser(l => Nil)

  val item: Parser[Char]  = Parser( l => l match {
      case Nil => Nil
      case x :: xs => List((x, xs))
  })

  def succ[A](a : A): Parser[A] = Parser(l => List((a, l)))

  def sat(p: Char => Boolean): Parser[Char] = 
    item.flatMap( x => 
        if (p(x)) 
        {
            succ(x) 
        }            
        else {
            fail
        }
    )

    val eof: Parser[Unit] = Parser{ l => l match {
        case Nil => List( ((), Nil))
        case _ => Nil
    }
    }

  val zero: Parser[Char] = sat(ch => ch == '0')
//   val nonZero: Parser[Char] = sat(ch => '1' <= ch && ch <= '9')
//   val digit: Parser[Char] = or(zero, nonZero)
//   val digits: Parser[List[Char]] = ???

  val numbers:Parser[Unit] = 
  for {
      _ <- zero
      _ <- eof
    } yield ()

    println(isNumber("0"))
}
