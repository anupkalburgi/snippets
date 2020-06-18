package main.scala.lcats.json

trait Json
final case class JsObject(get: Map[String, Json]) extends Json
final case class JsonString(get: String) extends Json
final case class JsNumber(get: Double) extends Json
case object JsNull extends Json

trait JsonWriter[A] {
  def write(value: A): Json
}

// Interface Syntax
object JsonSyntax {
  implicit class JsonWriterOps[A](value: A) {
    def toJson(implicit w: JsonWriter[A]): Json = 
      w.write(value)
  } 
}