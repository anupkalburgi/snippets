package snippet

object Solution extends App {

  def isNumber(s: String): Boolean = {
    number.runP(s.trim.toList) match {
      case Nil => false
      case cs =>
        println(cs)
        true
    }
  }

  case class Parser[+A](runP: List[Char] => List[(A, List[Char])]) {
    def map[B](f: A => B): Parser[B] =
      Parser(l =>
        runP(l) match {
          case Nil => Nil
          case xs  => xs.map(x => (f(x._1), x._2))
        }
      )

    def flatMap[B](f: A => Parser[B]): Parser[B] =
      Parser(l =>
        runP(l) match {
          case Nil => Nil
          case xs  => xs.flatMap(x => f(x._1).runP(x._2))
        }
      )
  }

  val fail = Parser(l => Nil)
  def succ[A](a: A): Parser[A] = Parser(l => List((a, l)))
  val item: Parser[Char] = Parser(l =>
    l match {
      case Nil     => Nil
      case x :: xs => List((x, xs))
    }
  )

  def sat(p: Char => Boolean): Parser[Char] =
    item.flatMap(x => {
      if (p(x)) {
        succ(x)
      } else {
        fail
      }
    })

  val eof: Parser[Unit] = Parser(l =>
    l match {
      case Nil => List(((), Nil))
      case _   => Nil
    }
  )

  def or[A](p1: Parser[A], p2: Parser[A]): Parser[A] =
    Parser(l => p1.runP(l) ++ p2.runP(l))

  def many[A](p: Parser[A]): Parser[List[A]] = or(succ(Nil), many1(p))

  def many1[A](p: Parser[A]): Parser[List[A]] =
    for {
      x <- p
      xs <- many(p)
    } yield x :: xs

  val zero: Parser[Char] = sat(ch => ch == '0')
  val nonZero: Parser[Char] = sat(ch => '1' <= ch && ch <= '9')
  val digit: Parser[Char] = or(zero, nonZero)
  val e: Parser[Char] = sat(ch => ch == 'e')
  val positive: Parser[Char] = sat(ch => ch == '+')
  val negative: Parser[Char] = sat(ch => ch == '-')
  val dot: Parser[Char] = sat(ch => ch == '.')

  val digits: Parser[List[Char]] = many1(digit)

  def repeat[A](a: Parser[A], n: Int): Parser[List[A]] = {
    if (n == 0) {
      succ(Nil)
    } else {
      for {
        x <- a
        xs <- repeat(a, n - 1)
      } yield x :: xs
    }
  }

  def atMost[A](a: Parser[A], n: Int): Parser[List[A]] = {
    if (n == 0) {
      succ(Nil)
    } else {
      or(repeat(a, n), atMost(a, n - 1))
    }
  }

  def base: Parser[Any] =
    or(for {
      _ <- digits
      _ <- dot
      _ <- digits
    } yield (), or(for {
      _ <- digits
      _ <- dot
    } yield (), or(for {
      _ <- dot
      _ <- digits
    } yield (), digits)))

  val number: Parser[Unit] = for {
    _ <- atMost(or(positive, negative), 1)
    _ <- base
    _ <- atMost(for {
      _ <- e
      _ <- atMost(or(positive, negative), 1)
      _ <- digits
    } yield (), 1)
    _ <- eof
  } yield ()

  println(isNumber("10"))
}
