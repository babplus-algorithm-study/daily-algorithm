```java
import java.util.*;

public class Main {

	static int N;
	static int logN;
	static Node[][] parents;
	
	static int[] ants;
	
	static ArrayList<Node>[] lists;
	
	public static void main(String[] args) throws Exception {
    	
		N = read();
    	
		ants = new int[N + 1];
		logN = (int) (Math.log(N) / Math.log(2));
		
		lists = new ArrayList[N + 1];
		
		
		parents = new Node[N + 1][logN + 1];
		for(int i = 1; i <= N; i++) {
			lists[i] = new ArrayList<>();
			ants[i] = read();
		}
		
		
		for(int i = 1; i < N; i++) {
			int a = read();
			int b = read();
			int c = read();
			
			lists[a].add(new Node(b, c));
			lists[b].add(new Node(a, c));
		}

		dfs(1, 0);
		parents[1][0] = new Node(0,0);
//		for(int i = 1; i <= N; i++) {
//			System.out.println(parents[i][0].index);
//		}

		for(int i = 1; i <= logN; i++) {
			for(int j = 1; j <= N; j++) {
				Node parent = parents[j][i-1];
				if(parent == null) continue;
				
				Node node = parents[parent.index][i-1];
				
				if(node == null) continue;
				
				parents[j][i] = new Node(node.index, parent.value + node.value);
			}
		}
		
		
		StringBuilder sb = new StringBuilder();
		for(int i = 1; i <= N; i++) {
			int ant = ants[i];
			int room = i;
			for(int j = logN; j >= 0; j--) {
				if(parents[room][j] == null) continue;
				
				if(parents[room][j].value > ant) continue;
				
				ant -= parents[room][j].value;
				room = parents[room][j].index;
				
			}
			
			sb.append(room == 0 ? 1 : room).append("\n");
		}
		
		System.out.println(sb);
		
		
    }
	
	public static void dfs(int node, int parent) {
		
		for(Node n : lists[node]) {
			if(n.index == parent) continue;
			parents[n.index][0] = new Node(node, n.value);
			dfs(n.index, node);
		}
		
	}
	
	private static class Node {
		int index;
		int value;
		
		public Node(int parent, int value) {
			this.index = parent;
			this.value = value;
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
