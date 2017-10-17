import java.util.Scanner;
import java.io.File;
import java.io.*;
import java.util.Arrays;

public class p22 {
public static void main(String[]args) {
	String names = "";
	String[] s = null;
	long score = 0;

		try {
			Scanner sc = new Scanner(new FileReader("p22_names.txt"));

			while(sc.hasNext()) {
				names = sc.next();
			}

			names = names.replace("\"", "").toUpperCase();
			s = names.split(",");
			Arrays.sort(s);

			}

		catch(FileNotFoundException  e) {
			System.out.println(e);
		}

		for(int i = 0; i < s.length; i++) {
			score += (long)(val(s[i]) * (i+1));
		}

		System.out.print("Total names score in the file: " + score);
	}

	public static int val(String s) {
		String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		int x = 0; s = s.toUpperCase();

			for(int i = 0; i < s.length(); i++) {
				x += alphabet.indexOf(String.valueOf(s.charAt(i)))+1;
			}

		return x;
	}


}