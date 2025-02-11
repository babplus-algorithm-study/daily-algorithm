```java
  import java.util.*;

import javax.xml.parsers.*;

import org.xml.sax.helpers.DefaultHandler;

import java.io.*;

public class Main {
	
	static int[] segments;
	static int[] lazy;
	static int N;
	static int size;

	public static void main(String[] args) throws Exception {
		
		
		int N = read();
		
		size = 1;
		while(size < N) {
			size <<= 1;
		}
		
		segments = new int[(size << 1) + 1];
		lazy = new int[(size << 1) + 1];
		for(int i = size + 1; i < size + N + 1; i++) {
			segments[i] = read();
		}
		
		
		int segmentSize = (size << 1);
		
		StringBuilder sb = new StringBuilder();
		
		while(segmentSize > 1) {
			segments[segmentSize >> 1] = segments[segmentSize] ^ segments[segmentSize-1];
			segmentSize-=2;
		}
		

		int M = read();
		
		for(int i = 0; i < M; i++) {
			int a = read();
			int b = read() + 1;
			int c = read() + 1;
			
			// 업데이트
			if(a == 1) {
				int d = read();
				update(b, c, 2, 1, size, d);

				
			} 
			// 출력
			else {
				
				sb.append(query(b, c, 2, 1, size)).append("\n");
			}
		}
		
		System.out.println(sb);
	}
	
	
	public static void updateLazy(int node) {
		
		if(node > size) {
			segments[node] ^= lazy[node];
			lazy[node] = 0;
			return;
		}
		
		lazy[(node << 1) - 1] ^= lazy[node];
		lazy[(node << 1)] ^= lazy[node];
		lazy[node] = 0;
		
	}
	
	public static boolean update(int left, int right, int node ,int start, int end, int val) {
		
		
		if(end < left || right < start) return false;
		
		if(left <= start && end <= right) {
			lazy[node] ^= val;
			updateLazy(node);
			return (end - start + 1) % 2 != 0;
		}
		
		int mid = (start + end) >> 1;
		boolean b = update(left, right, (node << 1) - 1, start, mid, val) ^ update(left, right, (node << 1), mid + 1, end, val);
		if(b) segments[node] ^= val;
		
		return b;
	}
	
	public static int query(int left, int right, int node, int start, int end) {
		
		if(lazy[node] != 0) updateLazy(node);
		
		if(end < left || right < start) return 0;
		
		if(left <= start && end <= right) {
			return segments[node];
		}
		
		int mid = (start + end) >> 1;
		return query(left, right, (node << 1) - 1, start, mid) ^ query(left, right, (node << 1), mid + 1, end);
	}
	
	 private static int read() throws Exception {
	        int d, o;
	        boolean negative = false;
	        d = System.in.read();
	        if (d == 45) {
	            negative = true;
	            d = System.in.read();
	        }

	        o = d & 15;
	        while ((d = System.in.read()) > 32)
	            o = (o << 3) + (o << 1) + (d & 15);

	        return negative ? -o : o;
	    }

}
```
