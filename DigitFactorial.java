public class DigitFactorial {
public static void main(String[]args) {

	for(int number=3; number<=100000; number++) {
	int sum = 0;
	int result = 0;
	String temp = String.valueOf(number);

	for(int i=0; i<=temp.length()-1; i++) {
		sum += facDigits((int)Character.getNumericValue(temp.charAt(i)));
		if(sum==number) {
			result += sum;
			System.out.println(result);
				}
			}
		}
	}
	public static int facDigits(int n) {
		if(n==1 || n==0) {
			return 1;
				}
		else {
			return n*facDigits(n-1);
				}

		}

}