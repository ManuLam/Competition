public class Two {
public static void main(String[]args) {
	int first = 1 , second = 1 , temp = 0 , n = 4000000 , even = 0;
	// 0 1 1 2 3 5

	for(int i=3; i<1000; i++) {
		temp = first + second;
		first = second;
		second = temp;
		if(temp%2==0) {
			even += temp;
		}

		if(even>n) {
		 break;
			}
	}

	System.out.print(even);

    }
}