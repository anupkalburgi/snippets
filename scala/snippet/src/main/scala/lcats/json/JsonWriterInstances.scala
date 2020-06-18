package main.scala.lcats.json

case class Person(name: String, email: String)

object PersonWriterInstance {
  implicit val stringWriter: JsonWriter[String] = new JsonWriter[String] {
    def write(value: String): Json = JsonString(value)
  }

  implicit val personWriter: JsonWriter[Person] = new JsonWriter[Person] {
    def write(value: Person): Json = JsObject(
      Map(
        "name" -> JsonString(value.name),
        "email" -> JsonString(value.email)
      )
    )
  }
}