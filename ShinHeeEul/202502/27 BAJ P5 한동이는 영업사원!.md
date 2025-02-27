```java
import java.io.*;
import java.util.*;

public class Solution {


    static int N;
    static int min = Integer.MAX_VALUE;
    static ArrayList<Integer>[] lists;
    static int[][] parents;
    static int[] depths;
    static boolean[] visited;
    static int count = 0;
    static int logN;
    
    public static void main(String[] args) throws Exception {
       
       N = read();
       
       logN = (int) (Math.log(N) / Math.log(2));
       lists = new ArrayList[N + 1];
       visited = new boolean[N + 1];
       parents = new int[N + 1][logN];
       depths = new int[N + 1];
       
       for(int i = 1; i < N + 1; i++) lists[i] = new ArrayList<>();
       
       for(int i = 1; i < N; i++) {
    	   
    	   int a = read();
    	   int b = read();
    	   
    	   lists[a].add(b);
    	   lists[b].add(a);
       }
       
       // 1. dfs 돌면서 맵 만들기
       dfs(1);
       // 2. parents 배열 채우기
       for(int i = 1; i < logN; i++) {
    	   for(int j = 1; j <= N; j++) {
    		   parents[j][i] = parents[parents[j][i - 1]][i - 1];
    	   }
       }
       
       int current = 1;
       int M = read();
       
       for(int i = 0; i < M; i++) {
           int destination = read();
           int tmp = destination;
           
           if(current == destination) continue;
           // 3. 높이 맞추기
           int dc = depths[current];
           int dd = depths[destination];
           
           if(dc < dd) {
        	   int diff = dd - dc;
        	   count += diff;
        	   destination = up(destination, diff);
           } else if(dd < dc) {
        	   int diff = dc - dd;
        	   count += diff;
        	   current = up(current, diff);
           }
           // 4. lca
           count += (lca(current, destination) << 1);
           current = tmp;
       }
       
       System.out.println(count);

    }
    
    public static int lca(int a, int b) {
    	// 제일 높은 거부터 하나씩 보면서
    	int cnt = 0;
    	for(int i = logN - 1; i >= 0; i--) {
    		if(parents[a][i] == parents[b][i]) continue;
    		
    		a = parents[a][i];
    		b = parents[b][i];
    		
    		cnt += Math.pow(2, i);
    	}
    	
    	return a == b ? cnt : cnt + 1;
    	
    }
    
    public static int up(int current, int diff) {
    	for(int i = 0; (1 << i) <= diff; i++) {
    		int bit = (1 << i);
    		if((bit | diff) == diff) {
    			current = parents[current][i];
    		}
    	}
    	return current;
    }
    
    public static void dfs(int start) {
    	Stack<Node> stack = new Stack<>();
    	
    	stack.add(new Node(start, 1));
    	visited[start] = true;
    	while(!stack.isEmpty()) {
    		Node node = stack.pop();
    		
    		int val = node.val;
    		int depth = node.depth;
    		depths[val] = depth;
    		
    		for(int child : lists[val]) {
    			if(visited[child]) continue;
    			parents[child][0] = val;
    			visited[child] = true;
    			stack.add(new Node(child, depth + 1));
    		}
    	}
    }
    
    static class Node {
    	int val;
    	int depth;
    	
    	public Node(int val, int depth) {
    		this.val = val;
    		this.depth = depth;
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
