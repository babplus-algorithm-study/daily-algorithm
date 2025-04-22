```java
import java.util.*;
import java.io.*;

class Main {

	
	public static void main(String[] args) throws Exception {
		
		int N = read();
		int K = read();
		// 세그 트리 만들고 몇개 세는지 카운트
		int MAX = (int) Math.pow(2, 24);
		for(int i = N; i <= MAX; i++) {
			if(query(1, i, 2, 1, MAX) <= K) {
				System.out.println(i - N);
				return;
			}
		}
		System.out.println(-1);
	}
	
	private static int query(int left, int right, int node, int start, int end) {
		if(end < left || right < start) return 0;
		
		if(left <= start && end <= right) {
			return 1;
		}
		
		int mid = (start + end) >> 1;
		return query(left, right, (node << 1) - 1, start, mid) + query(left, right, node << 1, mid + 1, end);
	}
	
	private static int read() throws Exception {
	    int c;
	    int n = 0;
	    boolean negative = false;

	    while ((c = System.in.read()) <= 32) {
	        if (c == -1) return -1;
	    }

	    if (c == '-') {
	        negative = true;
	        c = System.in.read();
	    }

	    do {
	        n = n * 10 + (c - '0');
	        c = System.in.read();
	    } while (c > 32);

	    return negative ? -n : n;
	}


}
```
