import java.util.ArrayList;                     // Importing an ArrayList to solve the solution by using it's built in functions
import java.math.BigInteger;
import java.lang.Math;

public class p29 {
public static void main(String[]args) {
	double temp = 0;
	ArrayList<Double> distinctTerms = new ArrayList<Double>();

	for(int a = 2; a <= 100; a++) {
		for(int b = 2; b <= 100; b++) {
			temp = Math.pow(a,b);                           // Allowing a variable to contain the power b to a, and later adding it onto distinctTerm

			if(!distinctTerms.contains(temp)) {       // A statement to find out duplicate numbers in our array, if not add the term to the ArrayList
				distinctTerms.add(temp);
			  }
			}
		}

		System.out.print(distinctTerms.size());     //Prints out the size (Unique numbers only) of the array (Answer = 9183)
    }
}