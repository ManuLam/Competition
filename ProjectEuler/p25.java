import java.math.BigInteger;                //Importing an object called Big Integer to store numbers beyond a "long" can hold
public class p25 {
public static void main(String[]args) {
	BigInteger AddSum1 = new BigInteger("1");
	BigInteger AddSum2 = new BigInteger("2");
	int Seq = 3;                               // Start count at 3 because there are 3 terms that are counted in the sequence already
	boolean T = true;

		while(T == true) {
		BigInteger sum = AddSum1.add(AddSum2);     // Creating a Fibonacci sequence where the sum is added onto the previous number
		AddSum1 = AddSum2;
		AddSum2 = sum;

		if(AddSum1.toString().length()==1000 || AddSum2.toString().length()==1000 ) {   // If the length of the number is 1000 digits long, the loop stops
			T = false;
			}
		Seq++;              // This counts the amount of Fibonacci terms that passed
		}

	System.out.println(AddSum2);
	System.out.println("\n" + Seq);          // Prints the amount of terms that were passed before it reached the 1000 digit term (Answer = 4782)
    }
}