import java.util.Scanner;
public class p18 {
public static int max = 0;
public static void main(String[]args) {
	Scanner in = new Scanner(System.in);
	int n = 3;
	int[][] a = new int[n][n];
	int x = 0, r = 0;
	int i = 0;

		while(i < n) {
			for(i = 0; i <= x; i++) {		// 0 >>> 14
				a[r][i] = in.nextInt();
			}
			r++;
			x++;
		}

		for(int k = 0; k < n; k++) {
			for(int j = 0; j < n; j++) {
				System.out.print(a[k][j]+ " ");
			}
			System.out.println();
		}

	rec(a, 0, 0, 0);
	System.out.print(max);

    }

	public static int rec(int[][] a, int r, int c, int sum) {
		if(r > a.length-1) {
			return 0;
		}

			sum += a[r][c];
			if(sum > max) max = sum;
		return rec(a, r+1, c, sum) & rec(a, r+1, c+1, sum);
	}

}