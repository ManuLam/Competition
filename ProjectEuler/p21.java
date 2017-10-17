public class p21 {
public static void main(String[]args) {
	int n = 10000;
	int sum = 0;

	for(int i = 1; i < n; i++) {
		if(amicable(i)) sum += i;
	}
		System.out.println("Total sum of all amicable numbers under 10000: "+sum);

 }

	public static boolean amicable(int x) {
		int sum = 0 , sum2 = 0;
		for(int i = 1; i <= x/2; i++) {
			if(x%i == 0) sum += i;
		}
		if(sum == x) return false;

		for(int i = 1; i <= sum/2; i++) {
			if(sum%i == 0) sum2 += i;
		}

		return (sum2 == x) ? true : false;

	}


}