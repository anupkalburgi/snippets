package snippet

  
import org.scalatest.funsuite.AnyFunSuite

class HelloSuite extends AnyFunSuite {

    test("Test that ‘Hello’ string is correct") {
        assert("Hello, world" == "Hello, world")
    }

    test ("Another test ...") (pending)

}