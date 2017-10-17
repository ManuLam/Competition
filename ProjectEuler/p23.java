public class p23 {
public static void main(String[]args) {
	int[] ab = new int[10000];
	boolean[] ex = new boolean[28124];
	int n = 28123 , count = 0, sumNon = 0;

	for(int i = 12; i < n; i++) {
		int sum = 0;
		for(int j = 2; j <= i/2; j++) {
			if(i%j == 0) sum += j;
		}
		if(sum > i) {
			ab[count] = i;
			count++;
		}
	}

	for(int i = 0; i < count; i++) {
		for(int j = 0; j < count; j++) {
			if((ab[i] + ab[j]) > n) break;
			if((ab[i] + ab[j]) <= n) ex[ab[i]+ab[j]] = true;
		}
	}

	for(int i = 0; i < n; i++) {
		if(!ex[i]) sumNon += i;
	}

	System.out.print("The sum of all the positive integers which cannot be written as the sum of two abundant numbers: "+sumNon);
	}
}