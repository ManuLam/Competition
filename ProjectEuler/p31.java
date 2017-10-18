public class p31 {
public static void main(String[]args) {
	int sum = 200;
	int[] a = {1,2,5,10,20,50,100,200};
	int[] ways = new int[sum+1];
	ways[0] = 1;

		for(int i = 0; i < a.length; i++) {
			for(int j = a[i]; j <= sum; j++) {
				ways[j] += ways[j-a[i]];
			}
		}

		System.out.println(ways[ways.length-1]);

    }


}