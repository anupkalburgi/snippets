package main.scala.lcats.printable

trait Printable[A] {
  def format(a: A): String
}

object Printable {
  def format[A](value: A)(implicit w: Printable[A]): String = w.format(value)
  def print[A](value: A)(implicit w: Printable[A]): Unit =
    println(format(value))
  def formatCat[Cat](value: Cat)(implicit w: Printable[Cat]): String =
    w.format(value)
}

object PrintableSyntax {
  implicit class PrintableOps[A](value: A) {
    def format(implicit w: Printable[A]): String = w.format(value)
    def print(implicit w: Printable[A]): Unit =
      println(w.format(value))
  }
}
