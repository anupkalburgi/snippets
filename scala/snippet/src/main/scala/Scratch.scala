package main.scala

import fastparse._, NoWhitespace._
object Scratch extends App {


    def parseA[_: P] = P("hello")

    val tmps: Parsed[Unit] = fastparse.parse("he", parseA(_))
    
    println(tmps)
}