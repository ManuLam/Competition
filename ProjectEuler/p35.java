import java.math.*;
public class p35 {
public static void main(String[]args) {
	int n = 1000000;
	int count = 0;
	int countSix = 0;

	for(int i = 2 ; i < n; i++) {
		if(rotationsPrime(i)) {
			count++;
			System.out.println(i);
			}
    	}

    	System.out.println(count);

	}


	public static boolean rotationsPrime(int x) {
		String n = String.valueOf(x);
		String[] tempR = new String[n.length()];
		tempR[0] = n;

		for(int k = 1; k < n.length(); k++) {
			String temp = "";

				temp += n.charAt(n.length()-1);
				temp += n.substring(0, n.length()-1);

				tempR[k] = temp;
				n = temp;
		}

		for(int i = 0; i < tempR.length; i++) {
		if(isPrimeOrEven(Integer.parseInt(tempR[i])) == false) return false;
		}

		return true;
	}

	public static boolean isPrimeOrEven(int x) {
		for(int i = 2; i < Math.sqrt(x); i++) {
			if(x%i == 0) return false;
		}

		String s = String.valueOf(x);

		for(int k = s.length()-1; k >= 0; k--) {
		if(s.charAt(k)%2 == 0)  return false;
		}

		return true;
	}


}

