import java.util.ArrayList;
public class p47 {
public static void main(String[]args) {
	ArrayList<Integer> primes = new ArrayList<Integer>();
	int n = 1 , c = 1, aim = 4;

	   for(int i = 2; i < 10000; i++) {
			if(isPrime(i)) primes.add(i);
		}

       while (c < aim) {
                if(primeFactor(n, primes) >= aim) c++;
                else c = 0;
                n++;
            }

            System.out.println(n-4);
	}

    public static boolean isPrime(int x) {
    	for(int i = 2; i <= Math.sqrt(x); i++) {
    		if(x%i == 0) return false;
    	}
    	return true;
    }

    public static int primeFactor(int x, ArrayList<Integer> primes) {
		int k = x;
		int c = 0;
			for(int i = 0; i < primes.size(); i++) {
				if(primes.get(i) * 2 > x) {
	           		  return ++c;
	     		}

				boolean t = false;
				while(k % primes.get(i) == 0) {
					t = true;
					k /= primes.get(i);
				}

				if(t) c++;

				if(k == 1) return c;
				}

			return c;
	    }

}