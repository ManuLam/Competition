import java.util.ArrayList;

public class p46 {
public static void main(String[]args) {
	int n = 10000 , odd = 1 , p = 1;
	ArrayList<Integer> a = new ArrayList<Integer>();

		for(int i = 2; i < n; i++) {
			if(isPrime(i)) a.add(i);
		}

		boolean f = true;
		while(f) {
				odd += 2;
				int i = 1;
				f = false;

				while(odd >= a.get(i)) {
					if(twiceSquare(odd-a.get(i))) {
						f = true;
						break;
					}
					else p = odd;	//storing the smallest conjecture that couldn't fit the rule
					i++;
				}
			}

	System.out.println("The smallest odd composite that cannot be written as the sum of a prime and twice a square: " + p);
	}

	public static boolean twiceSquare(long x) {
		double sq = Math.sqrt(x/2);
		return sq == ((int)sq);

	}

	public static boolean isPrime(int x) {
		for(int i = 2; i <= Math.sqrt(x); i++) {
			if(x%i == 0) return false;
		}
		return true;
	}

}