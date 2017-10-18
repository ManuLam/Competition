public class p45 {
public static void main(String[]args) {
	int n = 60000;

    	for(int i = 2; i < n; i++) {
    		for(int j = 2; j < n; j++) {
    			if(triangle(i) == pentagonal(j)) {
    				for(int k = 0; k < n; k++) {
    					if(triangle(i) == pentagonal(j) && pentagonal(j) == hexagonal(k)) System.out.println("T"+i+" P" + j + " H"+ k+ " "+triangle(i) + " " + pentagonal(j) + " " + hexagonal(k));
    				}
    			}
    		}
    	}

    }


    public static long triangle(int x) {
    	return (long)x*(x+1)/2;
    }

    public static long pentagonal(int x) {
    	return (long)x*((3*x)-1)/2;
    }

    public static long hexagonal(int x) {
    	return (long)x*((2*x)-1);
    }


}