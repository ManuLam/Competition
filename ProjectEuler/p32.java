public class p32 {
public static void main(String[]args) {
	int n = 2000 , count = 0 , sum = 0;
	int[] a = new int[100];
		for(int i = 1; i < n; i++) {
			for(int j = 2; j < n; j++) {
				String s = "";
				s += String.valueOf(i) + String.valueOf(j) + String.valueOf(i*j);
					if(check(s) && !inArray(a, i*j)) {
							System.out.println(i+ " * "+j+" = "+i*j);
							sum += i*j;
							a[count] = i*j;
							count++;
					}
			}
		}
		System.out.print("Sum of all products whose whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital: "+sum);
	}

	public static boolean check(String s) {
		String num = "123456789";
		if(s.length() < 9) return false;

		for(int i = 0; i < num.length(); i++) {
			int count = 0;
			for(int j = 0; j < s.length(); j++) {
				if(s.charAt(j) == '0') return false;
				if(num.charAt(i) == s.charAt(j)) count++;
				if(count == 2) return false;
			}
		}

		return true;
	}

	public static boolean inArray(int[] a, int x) {
		for(int i = 0; i < a.length; i++) {
			if(a[i] == x) return true;
		}
		return false;
	}

}