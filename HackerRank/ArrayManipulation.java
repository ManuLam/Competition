//You are given a list(1-indexed) of size n, initialized with zeroes. You have to perform m operations on the list and output the maximum of final values of all the n
//elements in the list. For every operation, you are given three integers a, b and k and you have to add value k to all the elements ranging from index a to b (both inclusive).

//My answer consists of a "difference array" , by taking the letting location array[a-1] = k and array[b] = -k
//We can loop through the array and add all the k values and subtract the ones that have reached the b index
//By storing the max at the array's index at its highest value, we can determine the max value through the entire array

import java.util.Scanner;

public class ArrayManipulation {

    public static void main(String[]args) {
    	Scanner in = new Scanner(System.in);
    	int n = in.nextInt();	//array length input
    	int m = in.nextInt();	//total of sums input
    	long[] a = new long[n];
    	for(int i = 0; i < m; i++) {
    		int l = in.nextInt();	//lowerside
    		int r = in.nextInt();	//upperside
    		int sum = in.nextInt();	//sum to add
    		a[l-1] += sum;			//add the sum difference to start
    		if(r < n) a[r] -= sum;	//remove the sum difference where it ends
    	}

    	long max = 0;	//storing the max value
    	long temp = 0;	//temporary to determine max value

    	for(int i = 0; i < n; i++) {	//looping the array to find max value
    		temp += a[i];
    		if(temp > max) max = temp;
    	}
    	System.out.print(max);		//printing the max value out
    }


}