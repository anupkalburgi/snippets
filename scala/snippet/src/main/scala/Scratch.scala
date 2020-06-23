package snippet

object Scratch {

    val input = List("ate", "eat", "pat", "tea", "now")

    val out =  input
    .map(w => w.sorted)
    .groupBy(id)
    
    print(out)
  
}
