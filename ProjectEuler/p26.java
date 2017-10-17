import java.util.ArrayList;
public class p26 {
public static void main(String[]args) {
	ArrayList<Integer> a = new ArrayList<Integer>();
	int max = 0, n = 0;

		for(int x = 1000; x > 100; x--) {
			boolean cycle = false;
			int i = 0;
			a.clear();
			a.add(1%x);
			if(isPrime(x)) {
				while(!cycle) {
					if(checkCycle(a, mod(a.get(i)*10, x))) {
						if(a.size() > max) {
							max = a.size();
							n = x;
						}
						cycle = true;
						break;
					}
					a.add(mod(a.get(i)*10, x));
					i++;
				}
			}
		}

		System.out.println("The number: " + n + " has the maximum length of recurring digits: " + max);
    }

    public static int mod(int x, int y) {
    	return x%y;
    }

    public static boolean checkCycle(ArrayList a, int x) {
    	return (int)a.get(0) == x;
    }

    public static boolean isPrime(int x) {
    	for(int i = 2; i <= Math.sqrt(x); i++) {
    		if(x%i == 0) return false;
    	}
    	return true;
    }

}