public class p33 {
public static void main(String[]args) {
	double sum = 1;
	// 49/98
	//	12-19 , 22- 29
	//!10 , !11 , !20 , !22...
	//12 > 49 for N, 21 > 99 for D

		for(int i = 12; i < 50; i++) {
			for(int j = 21; j < 99; j++) {
				if(properties(i) && properties(j) && check(i, j) && i < j) {
					sum *= (double)i/j;
					System.out.println(i + "/" + j + " = " + (double)i/j);
				}
			}
		}

		System.out.println("The product of these four fractions's denominator is: " + sum);	// 0.010000000000000002 or 1/100
    }

    public static boolean check(int x, int y) {
    	int a  = x/10 , b = y%10;
		if((float)x/y == (float)a/b && x%10 == y/10) return true;	//System.out.println((float)x/y + " " +x + " "+ y +" " + (float)a/b +" " + a + " " +b);
    	return false;
    }

    public static boolean properties(int i) {
    	if(i >= 99 || i%10 == i/10 || i%10 == 0) return false;
    	return true;
    }

}