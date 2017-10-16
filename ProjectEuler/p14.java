public class p14 {
public static void main(String[]args){
	long longest = 0;
	long largest = 0;

	for(int i = 2; i <= 1000000; i++) {
		int count = 1;
		long seq = i;

		while(seq != 1) {
			if(seq%2==0) {			//given function when n is even
				 seq /= 2;
			}
			else if(seq%2!=0) {
				seq = (seq*3) + 1;	//given function when n is odd
			}
		count++;					//count the sequence length
		}

		if(count>longest) {			//storing the longest sequence
			longest = count;
			largest = i;
		}
	}

	System.out.println(largest+" is the Triangular number with the longest sequence: "+longest);

    }
}