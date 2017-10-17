public class p30 {
public static void main(String[]args) {
	int n = 300000;
	int sum = 0;

	for(int i = 2; i < n; i++) {

		if(powerFive(i)) {
			System.out.println(i);
			sum += i;
		}
	}

		System.out.println(sum);

    }


    public static boolean powerFive(int x) {
    	String s = String.valueOf(x);
    	int len = s.length();
    	int sum = 0;

    	for(int i = 0; i < len; i++) {
    		sum += Math.pow(Character.getNumericValue(s.charAt(i)), 5);
    	}

    	if(x == sum) return true;

    	return false;
    }


}