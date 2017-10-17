public class p17 {
public static void main(String[]args) {
	int n = 1000;
	int sum = 0;
	int[] a = new int[1001];
	//"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	//"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
	//"twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

	a[1] = 3; a[2] = 3; a[3] = 5; a[4] = 4; a[5] = 4; a[6] = 3; a[7] = 5; a[8] = 5; a[9] = 4;
	a[10] = 3; a[11] = 6; a[12] = 6; a[13] = 8; a[14] = 8; a[15] = 7; a[16] = 7; a[17] = 9; a[18] = 8; a[19] = 8;
	a[20] = 6; a[30] = 6; a[40] = 5; a[50] = 5; a[60] = 5; a[70] = 7; a[80] = 6; a[90] = 6;
	a[1000] = 11;

	int start = 1 , end = 1000 , total = 0;

		while(start <= end) {
			total += val(a, String.valueOf(start));
			start++;
		}

		System.out.print(total);	//val(a, String.valueOf("888")));
    }

	public static int val(int[] a, String s) {
		if(s.length() == 4) return a[1000]; // then 1000 , 300 , 20 , 1 ( 1000

		if(s.length() == 3) {	// charAt(0) = indexin(String[](counted))
			if(Integer.parseInt(s)%100 == 0) return a[Character.getNumericValue(s.charAt(0))] + 7;
			else if(Integer.parseInt(s)%100 != 0) return a[Character.getNumericValue(s.charAt(0))] + 10 + val(a, s.substring(1,s.length()));
		}

		if(s.length() == 2) {	// charAt(0) == 1 (a[]) + break; , charAt(0) == b([])
			if(s.charAt(0) == '1') return a[Integer.parseInt(s)];
			else return (a[Character.getNumericValue(s.charAt(0))*10] + a[Character.getNumericValue(s.charAt(1))]);
		}

		if(s.length() == 1) return a[Integer.parseInt(s)];// charAt(0) = index of (1-9 counted array)

		return 0;
	}

}