public class p27 {
public static void main(String[]args) {
	int i = 1000 , max = 0 , product = 0;

		for(int a = -1000 ; a < i; a++) {
			for(int b = -1000 ; b <= i; b++) {
					int n = 0;

					while(isPrime(a,b,n)) {
						if(isPrime(a,b,n)) n++;
						if(n > max) {
							max = n;
							product = a*b;
						}
					}
			}
		}

	System.out.print("The quadratic expression that produces the maximum number of primes for consecutive values of n length: " + max + " with a*b product of: " + product);
    }

    public static boolean isPrime(int a, int b, int n) {
    	int x = (int)Math.abs((int)Math.pow(n,2) + (n*a) + b);
    	for(int i = 2; i <= Math.sqrt(x); i++) {
    		if(x%i == 0) return false;
    	}
    	return true;
    }

}