public class Four {
public static void main(String[]args) {	// well 1000 x 1000 = 1,000,000 so the element <1 Million
	int sum = 0;

	for(int i=999; i>=900; i--) {
	for(int j=999; j>=900; j--) {
		sum = i*j;

		if(isPalindrome(sum)==true) {
			System.out.println(sum);
			break;
				}
			}
		}
	}

	public static boolean isPalindrome(int sum) {
		String temp = "";
		String rev = "";

		temp = temp.valueOf(sum);

		for(int i=temp.length()-1; i>=0; i--) {
			rev += temp.charAt(i);
				}
		if(temp.equals(rev)) {
			return true;
				}
		else {
			return false;
				}
		}

}