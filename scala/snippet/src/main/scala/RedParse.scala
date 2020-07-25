package main.scala

object RedParse {}

trait Parsers[ParseError, Parser[+_]] { self =>

  def run[A](p: Parser[A])(input: String): Either[ParseError, A]
  def or[A](a: Parser[A], b: Parser[A]): Parser[A]
  def listOfN[A](n: Int, p: Parser[A]): Parser[List[A]]

  def many[A](p: Parser[A]): Parser[List[A]]
  def many1[A](p: Parser[A]): Parser[List[A]]
  def product[A, B](pa: Parser[A], pb: Parser[B]): Parser[(A, B)]
  def map2[A, B, C](a: Parser[A], b: Parser[B])(f : (A, B) => C): Parser[C]
  def map[A, B](p: Parser[A])(f: A => B): Parser[B]

  def slice[A](p: Parser[A]): Parser[String]

  def char(c: Char): Parser[Char] = map(string(c.toString))(_.charAt(0))
  def numAs: Parser[Int] = map(many(slice(char('a'))))(_.size)
  def succeed[A](a: A): Parser[A] = map(string(""))(_ => a) // How is it different from lifting in haskell?

  def string(s: String): Parser[String]
  implicit def operators[A](p: Parser[A]) = ParserOps[A](p)
  implicit def asStringParser[A](a: A)(
      implicit f: A => Parser[String]
  ): ParserOps[String] = ParserOps(f(a))

  case class ParserOps[A](p: Parser[A]) {
    def |[B >: A](p2: Parser[B]): Parser[B] = self.or(p, p2)
    def or[B >: A](p2: Parser[B]): Parser[B] = self.or(p, p2)
  }
}
