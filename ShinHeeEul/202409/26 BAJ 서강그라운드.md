```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;

public class Main {

    static ArrayList<Node>[] list;
    static int[] dist;
    static boolean[] visited;
    public static void main(String[] args) throws Exception {
            int n = read();
            int m = read();
            int r = read();
            int[] items = new int[n];
            list = new ArrayList[n + 1];

            for(int i = 0; i < n; i++) {
                list[i + 1] = new ArrayList<>();
                items[i] = read();
            }
            for(int i = 0; i < r; i++) {
                int a = read();
                int b = read();
                int l = read();

                list[a].add(new Node(b, l));
                list[b].add(new Node(a, l));
            }

            int max = 0;
            for(int i = 1; i <= n; i++) {
                dist = new int[n + 1];
                Arrays.fill(dist, Integer.MAX_VALUE);
                visited = new boolean[n + 1];
                dist[i] = 0;
                dij(i);
                int tmp = 0;
                for(int j = 1; j <= n; j++) {
                    if(dist[j] <= m) {
                        tmp += items[j-1];
                    }
                }
                max = Math.max(max, tmp);
            }
        System.out.println(max);
    }

    public static void dij(int start) {

        PriorityQueue<Node> pq = new PriorityQueue<>();

        pq.add(new Node(start, 0));

        while(!pq.isEmpty()) {
            Node node = pq.poll();

            if(visited[node.index]) continue;
            visited[node.index] = true;

            for(Node next : list[node.index]) {
                if(dist[next.index] > next.val + dist[node.index]) {
                    dist[next.index] = next.val + dist[node.index];
                    pq.add(new Node(next.index, dist[next.index]));
                }
            }
        }
    }

    private static class Node implements Comparable<Node> {
        int index;
        int val;

        public Node(int index, int val) {
            this.index = index;
            this.val = val;
        }

        @Override
        public int compareTo(Node o) {
            return val - o.val;
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
