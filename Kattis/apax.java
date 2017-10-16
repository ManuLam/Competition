import java.util.Scanner;
public class apax {
public static void main(String[]args) {
	Scanner in = new Scanner(System.in);
	String s = in.next() , temp = String.valueOf(s.charAt(0));

		for(int i = 0; i < s.length()-1; i++) {
			if(s.charAt(i) != s.charAt(i+1)) temp += s.charAt(i+1);
		}

		System.out.print(temp);
    }
}