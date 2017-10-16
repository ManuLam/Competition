public class p6 {
public static void main(String[]args) {
	int i = 1 , n = 100;
	int sqSum = 0 , seriesSum = 0;

		while(i <= n) {
			sqSum += Math.pow(i, 2);
			seriesSum += i;
			i++;
		}

	System.out.println("Sum of squared " + sqSum);
	System.out.println("Series sum squared " + (int)Math.pow(seriesSum,2));
	System.out.println("Difference = " + ((int)Math.pow(seriesSum,2) - sqSum));
    }
}