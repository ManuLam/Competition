import java.util.Scanner;

public class abc {
public static void main(String[]args) {
	Scanner in = new Scanner(System.in);
	int a = in.nextInt(), b = in.nextInt(), c = in.nextInt();
	String s = in.next();
	int[] ar = new int[3];

		if(a > b) {
			int t = b;
			b = a;
			a = t;
		}

		if(b > c) {
			int t = c;
			c = b;
			b = t;
		}

		if(a > b) {
			int t = b;
			b = a;
			a = t;
		}

		ar[s.indexOf("A")] = a;	ar[s.indexOf("B")] = b;	ar[s.indexOf("C")] = c;

		for(Integer x : ar) {
			System.out.print(x+" ");
		}

	}

	public static void swap(int x, int y) {
		int t = x;
		x = y;
		y = x;
	}
}