```java
import java.io.*;
import java.util.*;

public class Main {

    
    static int[][] map;
    public static void main(String[] args) throws Exception {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	
    	
    	int dir = 0;
    	int[] di = {0, -1, 0, 1};
    	int[] dj = {-1, 0, 1, 0};
    	
    	
    	int i = 10000;
    	int j = 10000;
    	
    	
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int r1 = Integer.parseInt(st.nextToken()) + 5000;
    	int c1 = Integer.parseInt(st.nextToken()) + 5000;
    	int r2 = Integer.parseInt(st.nextToken()) + 5000;
    	int c2 = Integer.parseInt(st.nextToken()) + 5000;
    	
    	map = new int[r2 - r1 + 1][c2 - c1 + 1];
    	int cnt = 0;
    	int limit = 10001;
    	boolean bool = true;
    	
    	for(int a = 10001 * 10001 ; a > 0; a--) {
    		
    		if(i >= r1 && i <= r2 && j >= c1 && j <= c2) {
    			map[i - r1][j - c1] = a;
    		}
    		cnt++;
    		int nxti = i + di[dir];
    		int nxtj = j + dj[dir];
    		
    		if(cnt == limit) {
    			cnt = 0;
    			if(bool) {
    				bool = false;
    				limit--;
    			} else {
    				bool = true;
    			}
    			dir = (dir + 1) % 4;
    			i += di[dir];
    			j += dj[dir];
    			continue;
    		}
    		
    		i = nxti;
    		j = nxtj;
    	}

    	
    	StringBuilder sb = new StringBuilder();
    	int max = 0;
    	for(int a = 0; a < map.length; a++) {
    		for(int b = 0; b < map[0].length; b++) {
    			max = Math.max(map[a][b], max);
    		}
    	}
    	
    	int ans = 0;
    	while(max > 0) {
    		ans ++;
    		max /= 10;
    	}
    	
    	for(int a = 0; a < map.length; a++) {
    		for(int b = 0; b < map[0].length; b++) {
    			sb.append(String.format("%" + ans + "d", map[a][b])).append(" ");
    		}
    		sb.append("\n");
    	}
    	
    	System.out.println(sb);
    }

}
```
