```java
import java.io.*;
import java.util.*;

public class Main {

	static int[] failure;
	static int count = 0;
	static int pLength;
	static int tLength;
	static StringBuilder sb;
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] T = br.readLine().toCharArray();
		char[] P = br.readLine().toCharArray();
		
		pLength = P.length;
		tLength = T.length;
		
		failure = new int[P.length];
		sb = new StringBuilder();
		failureFunction(P);
		KMP(T, P);
		
		System.out.println(count);
		System.out.println(sb);
	}
	
	public static void failureFunction(char[] s) {
		
		int pIdx = 0;
		
		for(int index = 1; index < pLength; index++) {
			
			while(pIdx != 0 && s[index] != s[pIdx]) pIdx = failure[pIdx - 1];
			
			if(s[pIdx] == s[index]) {
				pIdx++;
				failure[index] = pIdx;
			}
		}
		
	}
	
	public static void KMP(char[] t, char[] p) {
		int pIdx = 0;
		
		for(int index = 0; index < tLength; index++) {
			
			while(pIdx != 0 && t[index] != p[pIdx]) pIdx = failure[pIdx - 1];
			
			if(t[index] == p[pIdx]) {
				if(pIdx == pLength - 1) {
					sb.append(index - pLength + 2).append(" ");
					count++;
					pIdx = failure[pIdx];
				} else {
					pIdx++;
				}
			}
		}
		
	}

}
```
