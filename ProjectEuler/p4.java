public class p4 {
public static void main(String[]args) {	// well 1000 x 1000 = 1,000,000 so the element <1 Million
	int max = 0;

	for(int i = 999; i >= 900; i--) {
	for(int j = 999; j >= 900; j--) {
		if(isPalindrome(i*j) && i*j > max) max = i*j;
			}
		}

		System.out.println("The largest palindrome made from the product of two 3-digit numbers: " + max);
	}

	public static boolean isPalindrome(int sum) {
		String temp = String.valueOf(sum);
		String rev = "";

			for(int i = temp.length()-1; i >= 0; i--) {
				rev += temp.charAt(i);
			}

		if(temp.equals(rev)) return true;

		return false;
	}

}