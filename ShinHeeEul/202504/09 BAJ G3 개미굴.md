```java
import java.util.*;
import java.io.*;

class Main {
	
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		Trie trie = new Trie();
		for(int i = 0; i < N; i++) {
			Trie in = trie;
			StringTokenizer st = new StringTokenizer(br.readLine());
			int K = Integer.parseInt(st.nextToken());
			for(int j = 0; j < K; j++) {
				String s = st.nextToken();
				
				// 이미 있을 때?
				Trie deep = in.children.get(s);
				
				if(deep == null) {
					in.children.put(s, new Trie());
					deep = in.children.get(s);
				}
				
				in = deep;
			}
		}
		backTracking(trie, 0);
		System.out.println(sb);
		
	}
	
	public static void backTracking(Trie trie, int depth) {
		
		String[] arr  = trie.children.keySet().toArray(new String[0]);
		Arrays.sort(arr);
		for(String s : arr) {
			for(int i = 0; i < depth; i++) {
				sb.append("--");
			}
			sb.append(s).append("\n");
			backTracking(trie.children.get(s), depth + 1);
		}
	}
	
	static class Trie {
		HashMap<String, Trie> children = new HashMap<>();
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
