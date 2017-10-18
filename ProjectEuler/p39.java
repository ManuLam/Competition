public class p39 {
public static void main(String[]args) {
	int[] a = new int[1000];
	int n = 500, high = 0, index = 0;

		for(int i = 1; i < n; i++) {
			for(int j = 1; j < n; j++) {
				int x = perimeter(i,j);
				if(x != -1 && x < 1000) a[x]++;
			}
		}

		for(int i = 0; i < a.length; i++) {
			if(a[i] > high) {
				index = i;
				high = a[i];
			}
		}
		System.out.println("The the number of solutions maximised: " + index + " with " + high + " ways");
	}

    public static int perimeter(int x, int y) {
    	double p = Math.sqrt(Math.pow(x,2) + Math.pow(y,2)) + x + y;
    	return (p == (int)p) ? (int)p : -1;
    }

}