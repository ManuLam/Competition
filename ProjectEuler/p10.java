import java.math.BigInteger;        //Importing an object to hold numbers larger than a "long"

public class p10 {
public static void main(String[]args) {
	int num = 2000000;         		// Target number to reach
	BigInteger sum = new BigInteger("2");

		for(int i = 3; i < num; i++) {
			if(isPrime(i)) sum = sum.add(BigInteger.valueOf(i));    // If the number doesn't divide evenly, then the number is unique and is a Prime because it's divisble only by itself and one
		}

	System.out.println("Sum of Primes below 2 Million is: "+sum);   // Prints the sum of the Prime numbers below 2 Million (Answer = 142913828922)
    }

    public static boolean isPrime(int x) {
    	for(int i = 2; i <= Math.sqrt(x); i++) {
    		if(x%i == 0) return false;
    	}
    	return true;
    }

}