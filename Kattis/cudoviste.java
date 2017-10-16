import java.util.Scanner;

public class cudoviste {
public static void main(String[]args) {
	Scanner in = new Scanner(System.in);
	int r = in.nextInt(), c = in.nextInt(), space = 0;
	int[][] a = new int[r][c];

		for(int i = 0; i < r; i++) {
			String s = in.next();
			for(int j = 0; j < c; j++) {
				a[i][j] = val(s.charAt(j));
			}
		}

		int[] b = new int[5];
		for(int i = 0; i < r-1; i++) {
			for(int j = 0; j < c-1; j++) {
				if(!anyBuildings(a, i, j)) {
					int x = checkCrushCount(a, i, j);
					if(x == 0) b[0]++;
					if(x == 1) b[1]++;
					if(x == 2) b[2]++;
					if(x == 3) b[3]++;
					if(x == 4) b[4]++;
				}

			}
		}

		for(Integer x : b) {
			System.out.println(x);
		}
    }

    public static int val(char c) {
    	int val = -1;
    	if(c == '.') val = 0;
    	if(c == 'X') val = 1;
    	if(c == '#') val = 2;
    	return val;
    }

    public static boolean anyBuildings(int[][] a, int r, int c) {
    	if(a[r][c] == 2 || a[r+1][c] == 2 || a[r][c+1] == 2 || a[r+1][c+1] == 2) return true;
    	return false;
    }

    public static int checkCrushCount(int[][] a, int r, int c) {
    	int x = 0;
			if(a[r][c] == 1) x++;
			if(a[r+1][c] == 1) x++;
			if(a[r][c+1] == 1) x++;
			if(a[r+1][c+1] == 1) x++;

    	return x;
    }

}
