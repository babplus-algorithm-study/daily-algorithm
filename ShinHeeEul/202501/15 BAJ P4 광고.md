```java
import java.util.*;
import java.io.*;

class Main
{

	static int[] table;
	static int count;
	static String s;
	static int N;
	public static void main(String args[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		s = br.readLine();
		table = new int[N];
		
		failureFunction();
		
		System.out.println(N - table[N-1]);
	}
	
	public static void failureFunction() {
		int pIdx = 0;
		char[] arr = s.toCharArray();
		for(int index = 1; index < N; index++) {
			
			while(pIdx != 0 && arr[index] != arr[pIdx]) pIdx = table[pIdx - 1];
			
			if(arr[index] == arr[pIdx]) {
				pIdx++;
				table[index] = pIdx;
			}
		}
	}
	
}
```
