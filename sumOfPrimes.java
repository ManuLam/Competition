public class sumOfPrimes {
public static void main(String[]args) {
	int sum = 0;
	int count = 0;

	for(int i=6; i<=90; i++) {
	boolean isPrime = true;
	double a = Math.sqrt((double)i);
	for(int j=2; j<=a; j++) {
		if(i%j==0) {
			isPrime = false;
			break;
				}
			}
		if(isPrime == true) {
			count++;
			sum += i;
			System.out.printf("%s ",i);
		}
	}
	System.out.println();
	System.out.println(count);
	System.out.println(sum);

    }
}