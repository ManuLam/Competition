import java.util.Scanner;

public class p11 {
public static void main(String[]args) {
	Scanner in = new Scanner(System.in);
	int product = 0;
	int[][] a = new int[20][20];

	for(int i = 0; i < a.length; i++) {
		for(int j = 0; j < a.length; j++) {
			a[i][j] = in.nextInt();
		}
	}
	//4

	for(int i = 0; i < a.length; i++) {			//left and right
		for(int j = 0; j < a.length-3; j++) {
			int sum = 1;
			sum *= a[i][j];	sum *= a[i][j+1];	sum *= a[i][j+2];	sum *= a[i][j+3];
			if(sum > product) product = sum;
		}
	}

	for(int i = 0; i < a.length-3; i++) {		//up and down
		for(int j = 0; j< a.length; j++) {
			int sum = 1;
			sum *= a[j][i];	sum *= a[j][i+1];	sum *= a[j][i+2];	sum *= a[j][i+3];
			if(sum > product) product = sum;
		}
	}

	for(int i = 0; i < a.length-3; i++) {		//diag going v>
		for(int j = 0; j < a.length-3; j++) {
			int sum = 1;
			sum *= a[i][j];	sum *= a[i+1][j+1];	sum *= a[i+2][j+2];	sum *= a[i+3][j+3];
			if(sum > product) product = sum;
		}
	}

	for(int i = a.length-1; i >= 3; i--) {		//diag going ^>
		for(int j = 0; j < a.length-3; j++) {
			int sum = 1;
			sum *= a[i][j];	sum *= a[i-1][j+1];	sum *= a[i-2][j+2];	sum *= a[i-3][j+3];
			if(sum > product) product = sum;
		}
	}

System.out.print(product);



    }

}