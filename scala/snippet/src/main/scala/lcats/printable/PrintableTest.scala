package main.scala.lcats.printable

import PrintableInstances._
import PrintableSyntax._
import cats.Show
import cats.instances.int._
import cats.syntax.show._

case class Cat(name: String, age: Int, color: String)

object PrintableTest extends App {
  val tmp: Double = 10.0
  val tmpStr = "thisis10"
  println(Printable.format(tmp))
  println(Printable.format(tmpStr))

  val cat = Cat("test", 20, "gray")
  cat.print
  
  val showInt = Show.apply[Int]
  println(showInt.show(30))

  20.show

}
