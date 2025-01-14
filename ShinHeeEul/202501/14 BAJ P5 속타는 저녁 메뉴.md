```java
import java.util.*;
import java.io.*;

class Main
{

	static int[] table;
	static int count;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		String pattern = br.readLine().replaceAll(" ", "");
		String tmp = br.readLine().replaceAll(" ", "");
		table = new int[N];
		
		String word = tmp + tmp.substring(0, N - 1);
		
		KMP_Table(pattern);
		KMP_Search(word, pattern);
		
		int a = GCD(count, N);
		System.out.println(count / a + "/" + N / a);
	}
	
	public static int GCD(int a, int b) {
		int cnt = 1;
		int min = Math.min(a, b);
		for(int i = 1; i <= min; i++) {
			if((a % min == 0) && (b % min == 0)) cnt = i;
		}
		return cnt;
	}
	
	public static void KMP_Table(String pattern) {
		
		// 접두사 인덱스
		int pIdx = 0;
		int length = pattern.length();
		char[] arr = pattern.toCharArray();
		
		// 접미사 인덱스
		for(int idx = 1; idx < length; idx++) {
			
			// 일치하지 않을 경우 일치하는 패턴 찾기
			while(pIdx != 0 && arr[idx] != arr[pIdx]) {
				pIdx = table[pIdx - 1];
			}
				
			// 일치하는 경우 pIdx 증가시켜주기
			if(arr[idx] == arr[pIdx]) {
				pIdx++;
				table[idx] = pIdx;
			}
		}
	}
	
	public static void KMP_Search(String word, String pattern) {
		
		// 접두사 인덱스
		int pIdx = 0;
		// 일치하는지 비교?
		char[] wordArr = word.toCharArray();
		char[] patternArr = pattern.toCharArray();
		for(int i = 0; i < word.length(); i++) {
			// 일치 안하면 접두사 패턴 찾으러 내려가고
			while(pIdx != 0 && patternArr[pIdx] != wordArr[i]) {
				pIdx = table[pIdx - 1];
			}
			// 만약 pIdx가 끝까지 갔으면? 일치 + 1 시켜주고?
			// pIdx = table[pIdx]로 하여 패턴이 일치하는 부분을 보지 않도록 한다
			if(wordArr[i] == patternArr[pIdx]) {
				if(pIdx == pattern.length() - 1) {
					count++;
					pIdx = table[pIdx];
					continue;
				}
				pIdx++;
				
			}
		}
	}
}
```
