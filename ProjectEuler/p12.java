import java.math.*;
public class p12 {
public static void main(String[]args) {
	long mx = 0l;

	for(int j = 0; j <100000; j++) {
		long tri = j*(j+1)/2;
		double rt = Math.sqrt((double)tri);
		int count = 0;

	for(int i = 1; i <= rt; i++) {
		if(tri%i == 0) {
			if(tri/i==i) count++;
			else count+=2;
			}
		}

		if(count > 500) {
			mx = tri;
			break;
			}

	}

System.out.print(mx);


    }

}