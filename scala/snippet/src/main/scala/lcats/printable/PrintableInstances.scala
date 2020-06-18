package main.scala.lcats.printable

object PrintableInstances {
  implicit val printableInt: Printable[Int] = new Printable[Int] {
    def format(a: Int): String = a.toString
  }

  implicit val printableString: Printable[String] = new Printable[String] {
    def format(a: String): String = a
  }

  implicit val printableDouble: Printable[Double] = new Printable[Double] {
      def format(a: Double): String = a.toString
  }

  implicit val printableCat: Printable[Cat] = new Printable[Cat] {
    def format(a: Cat): String = s"${a.name} is a ${a.age} year-old cat"
  }
}
