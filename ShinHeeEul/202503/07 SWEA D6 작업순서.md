``java
import java.io.*;
import java.util.*;

public class Solution {

	static int[] arr;
	
	static int V;
	static int E;
	
	static ArrayList<Integer>[] lists;
	static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        
        
        for(int t = 1; t <= 10; t++) {
        	sb.append("#").append(t).append(" ");
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	V = Integer.parseInt(st.nextToken());
        	E = Integer.parseInt(st.nextToken());
        	

            arr = new int[V + 1];
        	lists = new ArrayList[V + 1];
        	
        	for(int i = 1; i <= V; i++) {
        		lists[i] = new ArrayList<>();
        	}
        	 st = new StringTokenizer(br.readLine());
        	for(int i = 0; i < E; i++) {
        		int s = Integer.parseInt(st.nextToken());
        		int e = Integer.parseInt(st.nextToken());
        		
        		
        		arr[e]++;
        		lists[s].add(e);
        	}
        	topologySort();
        	sb.append("\n");

        	
        }
        System.out.println(sb);
        
    }
    
    public static void topologySort() {
    	Queue<Integer> queue = new LinkedList<>();
    	
    	for(int i = 1; i <= V; i++) {
    		if(arr[i] == 0) queue.add(i);
    	}
    	
    	while(!queue.isEmpty()) {
    		
    		int a = queue.poll();
    		sb.append(a).append(" ");
    		for(int l : lists[a]) {
    			arr[l]--;
    			
    			if(arr[l] == 0) {
    				queue.add(l);
    			}
    		}
    	}
    }


}
```
