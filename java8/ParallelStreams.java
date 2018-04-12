import java.util.List;
import java.util.Arrays;

public class ParallelStreams{
	public static void main(String[] args){
		List<Integer> intList = Arrays.asList(new Integer[]{1,3,5,7,9,11});
		intList.parallelStream().forEachOrdered(e -> System.out.println(e));
	}
}
