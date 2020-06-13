package snippet

  
import org.scalatest.funsuite.AnyFunSuite

class HelloSuite extends AnyFunSuite {

    test("Binrary adding, also needs an algorithms") {
        assert("Hello, world" == "Hello, world")
        val ll = List(1,0,0,1,1)
        val rr = List(1,1,1,0,1)
        assert (BinaryAdd.addBinary(ll.reverse, rr.reverse, 0, List.empty[Int]) == List(1, 1, 0, 0, 0, 0))
    }

    test ("Another test ...") (pending)

}