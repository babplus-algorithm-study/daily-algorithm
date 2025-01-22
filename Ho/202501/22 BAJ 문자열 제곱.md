``` java
import java.util.*;
import java.io.*;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		while(true) {
			String w = br.readLine();
			
			if(w.charAt(0) == '.') {
				break;
			}
			
			int[] f = new int[w.length() + 1];
			
			String w1 = "#" + w;
			
			f[0] = -1;		
			//실패 함수 구하기
			int j = 0;
			
			int maxIndex = 1;
			int maxLen = 0;
			
			
			for(int i = 1; i < w1.length(); i++) {
				
				//i는 w1의 인덱스
				j = f[i-1];
				while(j >= 0 && w1.charAt(i) != w1.charAt(j+1)) {
					j = f[j];
				}
				
				f[i] = j + 1;
				
				if(f[i] > maxLen) {
					maxIndex = i;
					maxLen = f[i];
				}
				
			}
			
			
			int gap = w.length() - f[w.length()];

			if(w.length() % gap != 0 || f[w.length()] == 0) {
				sb.append("1 \n");
			}
			else {
				if(gap == 1 && w1.charAt(1) != w1.charAt(2)) {
					sb.append("1 \n");
					continue;
				}
				sb.append(w.length()/gap + "\n");
			}
		}
		System.out.println(sb.toString());

	}

}
```
