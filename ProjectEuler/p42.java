import java.util.Scanner;
import java.io.File;
import java.io.*;

public class p42 {
public static void main(String[]args) {
	String names = "";
	String[] s = null;
	int tri = 0;

		try {
			Scanner sc = new Scanner(new FileReader("p042_words.txt"));

			while(sc.hasNext()) {
				names = sc.next();
			}

			names = names.replace("\"", "").toUpperCase();
			s = names.split(",");

			}

		catch(FileNotFoundException  e) {
			System.out.println(e);
		}

		for(int i = 0; i < s.length; i++) {
			if(isTriangle(val(s[i]))) {
				tri++;
			}
		}

		System.out.print("Total amount of Triangle words: " + tri);
	}

	public static int val(String s) {
		String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		int x = 0; s = s.toUpperCase();

			for(int i = 0; i < s.length(); i++) {
				x += alphabet.indexOf(String.valueOf(s.charAt(i)))+1;
			}

		return x;
	}

	public static boolean isTriangle(int x) {
		if(Math.sqrt((8*x) + 1) == (int)Math.sqrt((8*x) + 1)) return true;
		return false;
	}

}