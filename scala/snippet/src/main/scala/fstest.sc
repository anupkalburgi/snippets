import $ivy.`com.lihaoyi::fastparse:2.2.2`

import fastparse._, NoWhitespace._

def parser[_: P] = P("hello")

val tmp = fastparse.parse("hello", parser(_))