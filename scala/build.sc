import mill._, scalalib._ ,scalafmt._

object snippet extends ScalaModule with ScalafmtModule {

	object test extends Tests {
        def ivyDeps = Agg(
            ivy"org.scalactic::scalactic:3.1.1",
            ivy"org.scalatest::scalatest:3.1.1"
        )
        def testFrameworks = Seq("org.scalatest.tools.Framework")
	}
	

	def scalaVersion = "2.12.11"
	def scalacOptions = Seq("-Ydelambdafy:inline")
	def ivyDeps = Agg(
		ivy"com.lihaoyi::pprint:0.5.2",
		)
	def testFrameworks = Seq("org.scalatest.tools.Framework")

	object binary extends ScalaModule {
		def moduleDeps = Seq(snippet)
		def scalaVersion = "2.12.11"
		}
}
