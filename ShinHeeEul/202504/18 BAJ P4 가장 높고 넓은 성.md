```java
import java.util.*;
import java.io.*;

class Main {

	
	static Node[] arr;
	static int[] ans;
	static int N;
	static boolean[] visited;
	static int count = 0;
	public static void main(String[] args) throws Exception {
		
		N = read();
		
		arr = new Node[N];
		ans = new int[N];
		visited = new boolean[N];
		
		for(int i = 0; i < N; i++) {
			// Node 등록하고
			arr[i] = new Node(i, read(), read());
		}
		
		Arrays.sort(arr);
		
		int depth = 1;
		while(count < (N - 2)) {
			// 시작 지점 잡고?
			Node[] s = new Node[2];
			
			int cnt = 0;
			for(int i = 0; i < N; i++) {
				if(cnt > 1) break;
				if(visited[arr[i].idx]) continue;
				s[cnt] = arr[i];
				cnt++;
			}
			
			convexHull(depth, s);
			depth++;
		}
		
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < N; i++) {
			sb.append(ans[i]).append(" ");
		}
		System.out.println(sb);
	}
	
	public static void convexHull(int depth, Node[] s) {
		Stack<Node> stack = new Stack<>();
		Stack<Node> stack2 = new Stack<>();
		
		stack.add(s[0]);
		stack.add(s[1]);
		
		stack2.add(s[0]);
		stack2.add(s[1]);
		
		for(int i = 0; i < N; i++) {

			Node n = arr[i];
			if(visited[n.idx]) continue;
			
			int size;
			while((size = stack.size()) > 1) {
				int ccwResult = ccw(stack.get(size - 1), stack.get(size - 2), n);
				
				if(ccwResult < 0) {
					break;
				} else stack.pop();
			}
			stack.add(n);
			
			while((size = stack2.size()) > 1) {
				int ccwResult = ccw(stack2.get(size - 1), stack2.get(size - 2), n);
				
				if(ccwResult > 0) {
					break;
				} else stack2.pop();
			}
			stack2.add(n);
			
		}
		
		count += stack.size() + stack2.size() - 2;
		
		if(stack.size() > 2) {
		while(!stack.isEmpty()) {
			Node node = stack.pop();
			visited[node.idx] = true;
			ans[node.idx] = depth;
		}
		}
		
		if(stack2.size() > 2) {
		while(!stack2.isEmpty()) {
			Node node = stack2.pop();
			visited[node.idx] = true;
			ans[node.idx] = depth;
		}
		}
	}
	
	public static int ccw(Node n1, Node n2, Node n3) {
		return (n1.x * n2.y + n2.x * n3.y + n3.x * n1.y) - (n1.x * n3.y + n2.x * n1.y + n3.x * n2.y);
	}
	
	static class Node implements Comparable<Node> {
		int idx;
		int x;
		int y;
		
		public Node(int idx, int x, int y) {
			this.idx = idx;
			this.x = x;
			this.y = y;
		}
		
		@Override
		public int compareTo(Node o) {
			// TODO Auto-generated method stub
			
			if(this.x == o.x) {
				return this.y - o.y;
			}
			return this.x - o.x;
		}
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
