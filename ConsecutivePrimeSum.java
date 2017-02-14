public class ConsecutivePrimeSum {
public static void main(String[]args) {
	int sum = 0;
	int highPrime = 0;

	for(int num=6; num<=20000; num++) {
		boolean isPrime = true;
		double a = Math.sqrt((double)num);
		for(int i=2; i<=a; i++) {
			if(num%i==0) {
				isPrime = false;
				break;
					}
				}
			if(isPrime==true) {
				sum += num;
					if(prime(sum)==true && sum<=1000000) {
						highPrime = sum;
						System.out.println(highPrime+" prime state: "+num);
					}
				}
  	 		}
		}

  	 public static boolean prime(int n) {
  	 	boolean isPrime = true;
  	 	double a = Math.sqrt((double)n);
  	 	for(int i=2; i<=a; i++) {
  	 		if(n%i==0) {
  	 			isPrime = false;
  	 			break;
  	 		}
  	 		}
  	 	if(isPrime==true) {
  	 		return true;
  	 		}
  	 	else {
  	 		return false;
  	 		}
  	 }

}