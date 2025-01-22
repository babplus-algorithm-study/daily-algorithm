```java

import java.util.*;
import java.io.*;

public class Main {

	static String s = "";
	static int Length;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuilder sb = new StringBuilder();
		
		while(!(s = br.readLine()).equals(".")) {
			Length = s.length();
			int tmp = failureFunction(s);
			if(tmp == 0 || Length % tmp != 0) sb.append(1).append("\n");
			else sb.append(Length / tmp).append("\n");
		}
		System.out.println(sb);
	}
	
	public static int failureFunction(String ss) {
		
		int pIdx = 0;
		char[] arr = s.toCharArray();
		char[] sarr = ss.toCharArray();
		int tmp = 0;
		
		for(int idx = 1; idx < Length; idx++) {
			
			if(pIdx != 0 && (arr[pIdx] != sarr[idx])) {
				pIdx = 0;
				tmp = 0;
			}
			
			if(arr[pIdx] == sarr[idx]) {
				if(tmp == 0) tmp = idx;
				pIdx++;
			}
		}
		
		return tmp;
	}

	
}

```
