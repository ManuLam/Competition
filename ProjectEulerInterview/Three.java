public class Three {
public static void main(String[]args) {
	long num = 600851475143l;
	double rt = Math.sqrt((double)num);
	long sum = 1l; // cant mutliply by 0

	for(int i=2; i<=rt; i++) {
		if(num%i==0) {
			sum *= i;
			if(sum==num) {
			System.out.print(i);
				}
			}
		}

    }
}