public class p44 {
public static void main(String[]args) {
	int n = 10000;
	boolean t = false;

    	for(int i = 2; i < n; i++) {
    		for(int j = 2; j < n; j++) {
    			long sum = pentagonal(j) + pentagonal(i);
    			long dif = pentagonal(j) - pentagonal(i);

    			if(isPentagonal(sum) && isPentagonal(dif) && (sum != 0 || dif != 0)) {
    				System.out.println("The difference between Pk" + j + " and Pj" + i + " is: " + dif + " which is pentagonal");
    				t = true;
    				break;
    			}
    			if(t == true) break;
    		}
    	}


    }

    public static long pentagonal(long x) {
    	return (long)x*((3*x)-1)/2;
    }

    public static boolean isPentagonal(long x) {
    	return ((1+Math.sqrt(1+(24*x)))%6 == 0);
    }


}