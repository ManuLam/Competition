import java.util.Calendar;

public class p19 {
public static void main(String[]args) {
	int sundays = 0;
	Calendar c = Calendar.getInstance();

		for(int i = 1901; i <= 2000; i++) {
			for(int j = 1; j <= 12; j++) {
				c.set(i, j, 1);
				int day = c.get(Calendar.DAY_OF_WEEK);
				if(day == 1) sundays++;
			}
		}

		System.out.print(sundays);
	}
}