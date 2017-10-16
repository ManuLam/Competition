public class p15 {
public static void main(String[]args) {
	int grid = 20;
	long paths = 1l;

	for(int i = 0; i < grid; i++) {
		paths *= (2*grid) - i;
		paths /= i + 1;
 	}

	System.out.print(grid+ " grids: "+paths);

	}
}