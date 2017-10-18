public class p41 {
public static void main(String[]args) {
	long largest = 2;
	long start = System.currentTimeMillis();

	for(long i = 0; i < 9999999; i++) {
		if(isPrime(i) && isPandigital(i)) largest = i;
	}

	System.out.println(largest);

	long end = System.currentTimeMillis();
	System.out.println(end-start);
  }

	public static boolean isPrime(long x) {
		for(long i = 2; i <= Math.sqrt(x); i++) {
			if(x%i == 0) return false;
		}
		return true;
	}

	public static boolean isPandigital(long x) {
		char[] a = {'1','2','3','4','5','6','7','8','9'};
		String s = String.valueOf(x);

			for(int i = 0; i < s.length(); i++) {
				int c = 0;
				for(int j = 0; j < s.length(); j++) {
					if(a[i] == s.charAt(j)) c++;
					if((Character.getNumericValue(s.charAt(j)) > s.length())) return false;
					if(s.charAt(j) == '0') return false;
					if(c>1) return false;
				}
			}

		return true;
	}

}