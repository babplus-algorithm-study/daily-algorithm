```java
import java.io.*;
import java.util.*;

public class Main {
	
	static int[] minSegments;
	static int[] maxSegments;
	static int size;
	
    public static void main(String[] args) throws Exception{
        int N = read();
        int Q = read();
        size = 1;
        while(size < N) {
        	size <<= 1;
        }
        
        minSegments = new int[(size << 1) + 1];
        Arrays.fill(minSegments, Integer.MAX_VALUE);
        maxSegments = new int[(size << 1) + 1];
        
        for(int i = size + 1; i < size + N + 1; i++) {
        	int val = read();
        	minSegments[i] = val;
        	maxSegments[i] = val;
        }
        
        int segmentSize = minSegments.length - 1;
        
        while(segmentSize > 2) {
        	minSegments[segmentSize >> 1] = Math.min(minSegments[segmentSize], minSegments[segmentSize - 1]);
        	maxSegments[segmentSize >> 1] = Math.max(maxSegments[segmentSize], maxSegments[segmentSize - 1]);
        	segmentSize -= 2;
        }
        
        StringBuilder sb = new StringBuilder();
        while(Q --> 0) {
        	int a = read();
        	int b = read();
        	
        	int min = query(a, b, 2, 1, size, false);
        	int max = query(a, b, 2, 1, size, true);
        	sb.append(max - min).append("\n");
        	
        }

        System.out.println(sb);
    }
    
    public static int query(int left, int right, int node, int start, int end, boolean b) {
    	
    	if(end < left || right < start) {
    		return b ? 0 : Integer.MAX_VALUE;
    	}
    	
    	if(left <= start && end <= right) {
    		return b ? maxSegments[node] : minSegments[node];
    	}
    	
    	int mid = (start + end) >> 1;
    	
    	if(b) {
    		return Math.max(query(left, right, (node << 1) - 1, start, mid ,b),
    				query(left, right, (node << 1), mid + 1, end, b));
    	} else {
    		return Math.min(query(left, right, (node << 1) - 1, start, mid ,b),
    				query(left, right, (node << 1), mid + 1, end, b));
    	}
    }

    
    private static int read() throws Exception {
        int d, o;
        boolean negative = false;
        d = System.in.read();
        if (d == '-') {
            negative = true;
            d = System.in.read();
        }

        o = d & 15;
        while ((d = System.in.read()) > 32)
            o = (o << 3) + (o << 1) + (d & 15);

        return negative? -o:o;
    }
}
```
