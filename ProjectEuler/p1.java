public class p1 {
public static void main(String[]args) {
	int result=0;

		for(int i = 1; i < 1000; i++) {				//Looping from 1 to 1000
			if(i%5 == 0 && i%3 == 0) result += i;	//If the number is divisible by both 3 and 5, the number is added on
			else if(i%5 == 0 || i%3 == 0) 	result+=i;	//If the number is divisible by 3 or 5, the number is added on

	    }

      System.out.println("The sum of all multiples of 3 or 5 below 1000 = "+result);
      // if 3 and 5 is both divisble by a number then it is added once. (Answer = 233168)
	}
}