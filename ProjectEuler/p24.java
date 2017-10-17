public class p24 {
public static void main(String[]args) {
	int[] a = {0,1,2,3,4,5,6,7,8,9};
	int start = 1 , end = 1000000;

		while(start < end) {
			int n = a.length;
			int i = n-1;

			while(a[i-1] >= a[i]) {
				i--;
			}

			int	j = n;
			while(a[i-1] >= a[j-1]) {
				j--;
			}

			swap(a, i-1, j-1);

			i++;
			j = n;

			while(i < j) {
				swap(a, i-1, j-1);
				i++;
				j--;
			}

			start++;
		}

		for(Integer x : a) {
			System.out.print(x);
		}

	}



	public static void swap(int[] a, int x, int y) {
		int temp = a[x];
		a[x] = a[y];
		a[y] = temp;
	}

}