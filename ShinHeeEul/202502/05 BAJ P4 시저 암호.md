```java
import java.util.*;
import java.io.*;

public class Main {

	static int[] failure;
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int T = Integer.parseInt(br.readLine());

		StringBuilder sb = new StringBuilder();
		
		while(T --> 0) {
			ArrayList<Integer> list = new ArrayList<>();
			HashMap<Character, Integer> map = new HashMap<>();
			
			char[] A = br.readLine().toCharArray();
			char[] W = br.readLine().toCharArray();
			char[] S = br.readLine().toCharArray();
			int aLength = A.length;
			for(int i = 0; i < aLength; i++) {
				map.put(A[i], i);
			}
			failure = new int[W.length];

			failureFunction(W);
			
			for(int i = 0; i < aLength; i++) {
				if(i != 0) {
					for(int j = 0; j < S.length; j++) {
						S[j] = A[(map.get(S[j]) + 1) % aLength];
					}
				}
				
				if(kmp(S, W)) {
					list.add(i == 0 ? i : aLength - i);
				}
			}
			if(list.size() == 0) {
				sb.append("no solution").append("\n");
			} else if(list.size() == 1) {
				sb.append("unique: ").append(list.get(0)).append("\n");
			} else {
				Collections.sort(list);
				sb.append("ambiguous: ");
				for(int li : list) sb.append(li).append(" ");
				sb.append("\n");
			}
		}
		System.out.println(sb);
	}
	
	public static void failureFunction(char[] pattern) {
		
		int pIdx = 0;
		
		for(int i = 1; i < pattern.length; i++) {
			
			while(pIdx != 0 && pattern[pIdx] != pattern[i]) 
				pIdx = failure[pIdx - 1];
			
			if(pattern[pIdx] == pattern[i]) {
				failure[i] = ++pIdx;
			}
		}
	}
	
	public static boolean kmp(char[] s, char[] pattern) {
		int pIdx = 0;
		int max = 0;
		// ABCBBABC
		// ABC
		// 
		for(int i = 0; i < s.length; i++) {
			
			while(pIdx != 0 && pattern[pIdx] != s[i]) 
				pIdx = failure[pIdx - 1];
			
			if(pattern[pIdx] == s[i]) {
				if(pIdx == pattern.length - 1) {
					max++;
					pIdx = failure[pIdx];
				} else {
					pIdx++;
				}
			}
		}
		
		return max == 1;
	}

}
```
