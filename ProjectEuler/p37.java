public class p37 {
public static void main(String[]args) {
	int n = 2000000, sum = 0;

		for(int i = 10; i < n; i++) {
			if(splitPrimeL(String.valueOf(i)) && splitPrimeR(String.valueOf(i)))  sum += i;
		}
		System.out.println(sum);
    }



    public static boolean prime(int n) {
    	if(n == 1) return false;
    	for(int i = 2; i <= Math.sqrt((double)n); i++) {
    		if(n % i == 0) return false;
    	}
    	return true;
    }


    public static boolean splitPrimeL(String n) {
    	String s = n;
 		for(int i = 0; i < n.length(); i++) {
 			if(prime(Integer.parseInt(s))) s = s.substring(1,s.length());
 			else return false;
 		}
		return true;
    }

    public static boolean splitPrimeR(String n) {
    	String s = n;
 		for(int i = 0; i < n.length(); i++) {
 			if(prime(Integer.parseInt(s))) s = s.substring(0,s.length()-1);
 			else return false;
 		}
		return true;
    }

}