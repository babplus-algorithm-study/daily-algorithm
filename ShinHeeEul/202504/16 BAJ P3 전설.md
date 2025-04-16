```java
import java.util.*;
import java.io.*;

class Main {
	
	static StringBuilder sb = new StringBuilder();
	static String s;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		Trie color = new Trie();
		Map<String, Boolean> nickname = new TreeMap<>();
		
		int C = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());
		
		for(int i = 0; i < C; i++) {

			Trie in = color;
			String s = br.readLine();
			
			for(char c : s.toCharArray()) {
				Trie deep = in.children.get(c);
				
				if(deep == null) {
					in.children.put(c, new Trie());
					
					deep = in.children.get(c);
				}
				
				in = deep;
			}
			
			in.end = true;
			
		}
		
		for(int j = 0; j < N; j++) {
			String s = br.readLine();
			nickname.put(s, true);
			
			
		}
		
		
		
		int Q = Integer.parseInt(br.readLine());

		
		for(int i = 0; i < Q; i++) {
			s = br.readLine();
			
			Trie trie = color;
			boolean b = true;
			for(int j = 0; j < s.length(); j++) {
				Trie tr = trie.children.get(s.charAt(j));
				if(tr == null) break;
				
				if(tr.end) {
					if(nickname.getOrDefault(s.substring(j + 1),false)) {
						b = false;
						sb.append("Yes").append("\n");
						break;
					}
				}
				trie = tr;
			}
			
			if(b) {
				sb.append("No").append("\n");
			}
		}
		
		System.out.println(sb);
		
	}
	
	public static void backTracking(Trie trie, int depth) {
		
		Character[] arr  = trie.children.keySet().toArray(new Character[0]);
		Arrays.sort(arr);
		for(char s : arr) {
			for(int i = 0; i < depth; i++) {
				sb.append("--");
			}
			sb.append(s).append("\n");
			backTracking(trie.children.get(s), depth + 1);
		}
	}

	
	static class Trie {
		Map<Character, Trie> children = new TreeMap<>();
		boolean end;
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
