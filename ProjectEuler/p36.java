public class p36 {
public static void main(String[]args) {
	int n = 1000000;
	long sum = 0;

		for(int i = 1; i < n; i++) {
		String bin = Integer.toBinaryString(i);
			if(palinCheck(String.valueOf(i), bin)) sum += i;
		}

		System.out.println("The sum of all numbers, less than one million, which are palindromic in base 10 and base 2: "+sum);
    }

    public static boolean palinCheck(String n, String bin) {
    	boolean  pal = true , pal2 = true;

		if(bin.charAt(0) == 0 || n.charAt(0) == 0) return false;

    	for(int i = 0; i < n.length()/2; i++) {
    		if(n.charAt(i) != n.charAt(n.length()-1-i)) return false;
    	}

    	for(int i = 0; i < bin.length()/2; i++) {
    		if(bin.charAt(i) != bin.charAt(bin.length()-1-i)) return false;
    	}

    	return true;
    }


}