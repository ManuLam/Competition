public class p28 {
public static void main(String[]args) {
		System.out.println(diags(500)+1); // adding "1" onto sum since it is the cross/junction of our diagonals
    }

    public static int diags(int x) {
    	if(x == 0) return 0;
    	return (int)(4*Math.pow(((2*x)+1), 2) - (12*x)) + diags(x-1);
    }

}