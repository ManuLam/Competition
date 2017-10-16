public class p7 {
public static void main(String[]args) {
	int count = 0;

		for(int i = 2; i <= 5000000; i++) {
			if(isPrime(i)) count++;
			if(count == 10001) {
				System.out.println(i);
				break;
				}
			}

    }

    public static boolean isPrime(int x) {
    	for(int i = 2; i <= Math.sqrt(x); i++) {
    		if(x%i == 0) return false;
    	}
    	return true;
    }

}