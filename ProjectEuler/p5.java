public class p5 {
public static void main(String[]args) {
	int n = 300000000;

		for(int i = 1; i < n; i++) {
			for(int j = 1; j <= 20; j++) {
				if(i%j != 0) break;
				else if(i%j == 0 && j == 20) System.out.println("Smallest number divisible by all numbers from 1 to 20 is: " + i);
			}
		}


	 }
}