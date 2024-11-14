```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1647 {
    static int N,M;
    static PriorityQueue<Edge> pq = new PriorityQueue<>();
    static int[] unions;

    static class Edge implements Comparable<Edge>{
        int cost;
        int to;
        int from;

        public Edge(int cost, int to, int from) {
            this.cost = cost;
            this.to = to;
            this.from = from;
        }

        @Override
        public int compareTo(Edge o) {
            return cost - o.cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        unions = new int[N];
        int cnt = 0;
        for (int i = 0; i < N; i++) {
            unions[i] = i;
        }

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int to = Integer.parseInt(st.nextToken()) - 1;
            int from = Integer.parseInt(st.nextToken()) - 1;
            int cost = Integer.parseInt(st.nextToken());

            pq.add(new Edge(cost, to, from));
        }

        int sum = 0;

        while(!pq.isEmpty()) {
            Edge curEdge = pq.poll();
            if(cnt == N-1) break;
            if(find(curEdge.from) != find(curEdge.to)) {
                union(curEdge.from,curEdge.to);
                sum += curEdge.cost;
                cnt++;
                if(cnt == N-1) sum -= curEdge.cost;
            }
        }

        System.out.println(sum);
    }

    private static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a > b) {
            unions[a] = b;
        } else {
            unions[b] = a;
        }
    }

    private static int find(int x) {
        if (unions[x] == x)
            return x;
        else
            return unions[x] = find(unions[x]);
    }
}

```