public class Seven {
public static void main(String[]args) {
	int count = 0;

	for(int i=2; i<=5000000; i++) {
	boolean t = true;
	double a = Math.sqrt((double)i);
	for(int j=2; j<=a; j++) {

		if(i%j==0) {
			t = false;
			break;
	 		}
		}
		if(t==true) {
			count++;
				}
		if(count==10001) {
			System.out.println(i);
			break;
			}
		}

    }
}