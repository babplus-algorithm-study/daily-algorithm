```java
//달이 차오른다, 가자.
import java.util.*;
import java.io.*;

class Main {
	static int N;
	static int M;
	static char[][] map;
	static int[] di = {-1, 1, 0, 0};
	static int[] dj = {0, 0, 1, -1};
	static Node start;
	static boolean[][][] visited;
	 public static void main(String[] args) throws Exception {
	     
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		 StringTokenizer st = new StringTokenizer(br.readLine());
		 N = Integer.parseInt(st.nextToken());
		 M = Integer.parseInt(st.nextToken());
		 
		 map = new char[N][M];
		 
		 for(int i = 0; i < N; i++) {
			 String s = br.readLine();
			 for(int j = 0; j < M; j++) {
				 map[i][j] = s.charAt(j);
				 if(map[i][j] == '0') {
					 start = new Node(i, j, 0, 0);
					 map[i][j] = '.';					 
				 }
			 }
		 }
		 visited = new boolean[N][M][(1 << 6)];
		 
		 System.out.println(bfs());
	 }
	 
	 public static int bfs() {
		 
		 Queue<Node> queue = new LinkedList<>();
		 
		 visited[start.i][start.j][0] = true;
		 queue.add(start);
		 
		 while(!queue.isEmpty()) {
			 Node node = queue.poll();
			 
			 int i = node.i;
			 int j = node.j;
			 int depth = node.depth;
			 int key = node.key;
			 
			 
			 if(map[i][j] == '1') return depth;
			 
			 
			 for(int k = 0; k < 4; k++) {
				 Node newNode = new Node(i + di[k], j + dj[k], depth + 1, key);
				 
				 if(!check(newNode)) continue;
				 
				 int m = map[newNode.i][newNode.j];
				 visited[newNode.i][newNode.j][key] = true;
				 if(m >= 'a' && m <= 'z') {
					newNode.key = newNode.key | (1 << (m - 'a'));
					visited[newNode.i][newNode.j][key] = true;
				 }
				 
				 queue.add(newNode);
			 }
		 }
		 
		 
		 return -1;
	 }
	 
	 public static boolean check(Node node) {
		 int i = node.i;
		 int j = node.j;
		 int key = node.key;
		 if(i < 0 || j < 0 || i >= N || j >= M || map[i][j] == '#' || visited[i][j][key]) return false;
		 
		 if(map[i][j] >= 'A' && map[i][j] <= 'F') {
			 int bit = 1 << (map[i][j] - 'A');
			 
			 if((bit | key) != key) return false;
		 }
		 
		 return true;
	 }
	 
	 static class Node {
		 int i;
		 int j;
		 int depth;
		 int key;
		 
		 public Node(int i, int j, int depth, int key) {
			 this.i = i;
			 this.j = j;
			 this.depth = depth;
			 this.key = key;
		 }

		@Override
		public int hashCode() {
			// TODO Auto-generated method stub
			return super.hashCode();
		}

		@Override
		public boolean equals(Object obj) {
			// TODO Auto-generated method stub
			return super.equals(obj);
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
