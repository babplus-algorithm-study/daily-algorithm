```java
import java.io.*;
import java.util.*;

public class Main {

    static List<Node>[] lists;
    static int s;
    static int e;
    static boolean[] visited;
    public static void main(String[] args) throws Exception {
        int N = read();
        int M = read();

        lists = new List[N + 1];

        for(int i = 1; i <= N; i++) lists[i] = new ArrayList();

        for(int i = 0; i < M; i++) {
            int A = read();
            int B = read();
            int C = read();

            lists[A].add(new Node(B, C));
            lists[B].add(new Node(A, C));
        }

        int start = 1;
        int end = 1_000_000_001;

        s = read();
        e = read();

        while(start < end) {
            visited = new boolean[N + 1];
            int mid = (start + end) >> 1;
            visited[s] = true;
            if(dfs(s, mid)) start = mid + 1;
            else end = mid;
        }
        System.out.println(start - 1);
    }

    public static boolean dfs(int s, int val) {

        if(s == e) return true;

        for(Node n : lists[s]) {
            int i = n.to;
            if(visited[i] || n.val < val) continue;
            visited[i] = true;
            if(dfs(i, val)) return true;
        }

        return false;
    }

    static class Node {
        int to;
        int val;

        public Node(int to, int val) {
            this.to = to;
            this.val = val;
        }
    }

    private static int read() throws Exception {
        int d, o;
        boolean negative = false;
        d = System.in.read();
        if (d == 45) {
            negative = true;
            d = System.in.read();
        }

        o = d & 15;
        while ((d = System.in.read()) > 32)
            o = (o << 3) + (o << 1) + (d & 15);

        return negative ? -o : o;
    }
}

```
