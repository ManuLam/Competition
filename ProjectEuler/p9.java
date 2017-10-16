public class p9 {
public static void main(String[]args) {
	int num = 1000;
	int a = 1 , b = 1 , c = 0;

	for(int i = a; i <= 1000; i++) {
		for(int j = b; j <= 1000; j++) {
			double sum = 0;
			sum = Math.pow(i, 2) + Math.pow(j,2);

			if((Math.sqrt(sum) + i + j) == num ) {
				System.out.print("Target: " + (Math.sqrt(sum)+i+j)+" ");
				System.out.print("a: " + i + " ");
				System.out.print("b: " + j + " ");
				System.out.print("c: " + (Math.sqrt(sum))+" ");
				System.out.println("Product of a , b , c: " + i * j * (int)Math.sqrt(sum));
				break;
				}
			}
		}

    }
}