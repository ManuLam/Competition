public class p43 {
public static void main(String[]args) {
	int[] a = {0,1,2,3,4,5,6,7,8,9};
	long sum = 0;
	long start = 1 , end = 3628800;

		while(start < end) {
			int n = a.length;
			int i = n-1;

			while(a[i-1] >= a[i]) {
				i--;
			}

			int j = n;
			while(a[i-1] >= a[j-1]) {
				j--;
			}

			a = swap(a, i-1, j-1);
			i++;
			j = n;

			while(i < j) {
				a = swap(a , i-1, j-1);
					i++;
					j--;
			}

			String s = "";
			for(Integer x : a) {
				s += String.valueOf(x);
			}

			if(properties(s)) sum += Long.parseLong(s);

			start++;
		}

		System.out.println(sum);
}

	public static boolean properties(String s) {
		int[] a = {2,3,5,7,11,13,17};

		for(int i = 1; i < s.length()-2; i++) {
			if(Long.parseLong(s.substring(i,i+3))%a[i-1] != 0) return false;
		}

		return true;
	}

	public static int[] swap(int[] a, int x, int y) {
		int temp = a[x];
		a[x] = a[y];
		a[y] = temp;

		return a;
	}

}