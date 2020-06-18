package main.scala.lcats.json

import JsonSyntax._
import PersonWriterInstance._

object Test extends App {
    // println(Json.toJson(Person("jon", "jon@mail.com"))(personWriter)) 
    println(Person("dav", "dav@mail.com").toJson)
}