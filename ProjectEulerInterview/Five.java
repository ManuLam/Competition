public class Five {
public static void main(String[]args) { // a number all divisble by  -> 20 [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
	// First by taking all the Prime numbers and mutliplying them together
	// Second find the max power of 2 , 3 which is up to 20
	// Multiply.

	int sum = 1 , temp1 = 0 , temp2 = 0;

	for(int i=4; i<=20; i++) {
	boolean t = true;
	double a = Math.sqrt((double)i);
	for(int j=2; j<=a; j++) {
		if(i%j==0) {
			t = false;
			break;
				}
		}
		if(t==true) {
			sum *= i;
		}
	}

	for(int i=0; i<5; i++) {
		if(Math.pow(2,i)<20) {
			temp1 = i;
		}
		if(Math.pow(3,i)<20) {
			temp2 = i;
		}
	}

		sum *= Math.pow(2,temp1);
		sum *= Math.pow(3,temp2);

	System.out.println(sum);

    }
}