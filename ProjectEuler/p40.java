public class p40 {
public static void main(String[]args) {
	String s = ".";
	long sum = 1;
	long start = System.currentTimeMillis();

	for(int i = 1; i < 1000000; i++) {
		s += String.valueOf(i);
		}
	sum *= Long.parseLong(s.substring(1,2));
	sum *= Long.parseLong(s.substring(10,11));
	sum *= Long.parseLong(s.substring(100,101));
	sum *= Long.parseLong(s.substring(1000,1001));
	sum *= Long.parseLong(s.substring(10000,10001));
	sum *= Long.parseLong(s.substring(100000,100001));
	sum *= Long.parseLong(s.substring(1000000,1000001));

System.out.print(sum);
	long end = System.currentTimeMillis();

	System.out.println(end-start);

}
}