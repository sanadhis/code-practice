object Euler {

    def main(args: Array[String]) {
        val sc = new java.util.Scanner (System.in);
        var n = sc.nextInt();
        var a0 = 0;
        while(a0 < n){
            var x = sc.nextDouble();
            println("%.4f".format(euler(x,0)))
            a0+=1;
        }
    }
    
    def factorial(n:Int) : Int =  {
        if (n==0 || n==1){
            return 1
        }
        else{
            return n * factorial(n-1)
        }
    }
    
    def euler(n: Double, m:Int) : Double = {
        if(m == 10){
            return 0
        }
        else{
            return (Math.pow(n,m) / factorial(m)) + euler(n,m+1)
        }
    }
}

