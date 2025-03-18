```java

import java.io.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.*;

public class Main {

	
	static int[] segments;
	static int size;
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    private static int read() throws Exception {
        return Integer.parseInt(br.readLine().trim());
    }

    public static void main(String[] args) throws Exception {
        int T = read(); // 테스트 케이스 개수
        
        StringBuilder sb = new StringBuilder();
        
        for (int t = 0; t < T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int B = Integer.parseInt(st.nextToken());
            int P = Integer.parseInt(st.nextToken());
            int Q = Integer.parseInt(st.nextToken());

            size = 1;
            while (size < B) {
                size <<= 1;
            }

            segments = new int[(size << 1) + 1];

            for (int q = 0; q < P + Q; q++) {
                st = new StringTokenizer(br.readLine());
                char c = st.nextToken().charAt(0);
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());

                if (c == 'P') {
                    update(a, b);
                } else {
                    sb.append(query(a, b, 2, 1, size)).append("\n");
                }
            }
        }

        System.out.print(sb); // 출력 최적화
    }
	
	public static void update(int idx, int val) {
		
		idx += size;
		
		while(idx > 2) {
			segments[idx] += val;
			idx = (idx + 1) >> 1;
		}
		
	}
	
	public static int query(int left, int right, int node, int start, int end) {
		if(left > end || right < start) return 0;
		
		if(left <= start && end <= right) {
			return segments[node];
		}
		
		int mid = (start + end) >> 1;
		
		return query(left, right, (node << 1) - 1, start, mid) + query(left, right, node << 1, mid + 1, end);
	}
	

}

```
