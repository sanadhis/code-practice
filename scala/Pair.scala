object Pair{
    def main(args: Array[String]): Unit = {
        var x = List.range(1,5)
        var y = List.range(6,10)
        (x,y).zipped.map((e,i) => println(e + " " + i) )
    }
}