import java.util.Arrays;
public class p49 {
public static void main(String[]args) {
	int n = 10000 , p = 3330;

		for(int i = 1488; i < n; i++) {
			boolean a = isPrime(i), b = isPrime(i+p), c = isPrime(i+(p*2));

			if(a && b && c) {
				String d = String.valueOf(i), e = String.valueOf(i+p), f = String.valueOf(i+(p*2));
				if(pandigitEqual(d, e, f))	{
					System.out.println("The next 12-digit number you form by concatenating the three terms: " + i + (i+p) + (i+(p*2)));
					break;
				}
			}
		}

	}

    public static boolean isPrime(int x) {
    	if(x == 0) return false;
    	for(int i = 2; i < Math.sqrt(x); i++) {
    		if(x%i == 0) return false;
    	}

    	return true;
    }

    public static boolean pandigitEqual(String d, String e, String f) {
    	char[] nums1 = d.toCharArray();
    	char[] nums2 = e.toCharArray();
    	char[] nums3 = f.toCharArray();

			Arrays.sort(nums1);
			Arrays.sort(nums2);
			Arrays.sort(nums3);
			for(int i = 0; i < nums1.length; i++) {
				if(nums1[i] != nums2[i] && nums1[i] != nums3[i]) return false;
	  		 }
    	return true;
    }

}