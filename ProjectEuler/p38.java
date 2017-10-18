public class p38 {
public static void main(String[]args) {
		String max = "";

		for(int i = 0; i < 10000; i++) {
			String s = "";
			for(int j = 1; j < 25; j++) {
				s += String.valueOf(i*j);
					if(s.length() == 9 && sumPandigital(s)) max = s;
			}
		}

		System.out.print("The Largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer: " + max);
    }


    public static boolean sumPandigital(String s) {
    	char[] ch = {'1','2','3','4','5','6','7','8','9'};

    		for(int i = 0; i < ch.length; i++) {
    			int c = 0;
    			for(int j = 0; j < s.length(); j++) {
    			if(s.charAt(j) == ch[i]) c++;
    			if(s.charAt(j) == '0') return false;
    			if(c > 1) return false;
    			}
    		}

    	return true;

    }


}