public class p50 {
public static void main(String[]args) {
	int sum = 0 , highPrime = 0 , x = 0;

	for(int num=6; num <= 20000; num++) {
			if(isPrime(num)) {
			sum += num;
				if(isPrime(sum) && sum <= 1000000) {
					highPrime = sum;
					x = num;
					}
				}
  	 		}

  	 		System.out.println(highPrime + " Prime state: " + x);
		}

  	 public static boolean isPrime(int n) {
  	 	for(int i = 2; i <= Math.sqrt(n); i++) {
  	 		if(n%i == 0) return false;
  	 	}
  	 	return true;
  	 }

}