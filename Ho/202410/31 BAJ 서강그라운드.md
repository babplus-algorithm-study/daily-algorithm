```java
package baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P14938 {
    static int N;
    static int M;
    static int R;

    static ArrayList<Edge>[] lists;
    static int[] items;
    static int[] dist;

    static class Edge {
        int weight;
        int start;
        int end;

        Edge(int weight, int start, int end) {
            this.weight = weight;
            this.start = start;
            this.end = end;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        lists = new ArrayList[N];
        items = new int[N];
        dist = new int[N];

        for(int i = 0; i < N; i++) {
            lists[i] = new ArrayList<>();
            items[i] = Integer.parseInt(st.nextToken());
        }

        for(int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());

            int s = Integer.parseInt(st.nextToken()) - 1;
            int e = Integer.parseInt(st.nextToken()) - 1;
            int w = Integer.parseInt(st.nextToken());

            lists[s].add(new Edge(w, s, e));
            lists[e].add(new Edge(w, e, s));
        }
        // 여기까지 초기 세팅
        //풀이 방법 하나씩 내려보고 각 거리 측정한 다음 갈 수 있는 곳 아이템 개수 다 더하기

        int ans = 0;

        for(int i = 0; i < N; i++) {
            dijkstra(i);
            int temp = 0;
            for(int j = 0; j <N; j++) {
                if(dist[j] <= M) {
                    temp += items[j];
                }
            }
            ans = Math.max(ans, temp);
        }

        System.out.println(ans);
    }

    static public void dijkstra(int s) {
        //현재 정점에서 갈 수 있는 가장 가까운 정점들을 큐에 넣는거
        PriorityQueue<Node> pq = new PriorityQueue<>();

        for(int i = 0; i < N; i++) {
            dist[i] = (int) 1e9;
        }
        dist[s] = 0;
        pq.add(new Node(s, 0));

        while(!pq.isEmpty()) {
            Node cur = pq.poll();

            if(dist[cur.vertex] != cur.cost) continue;

            for(int i = 0; i < lists[cur.vertex].size(); i++) {
                // 현재 정점과 연결된 간선은 모두 체크하기
                Edge nextEdge = lists[cur.vertex].get(i);
                int newCost = dist[cur.vertex] + nextEdge.weight;

                if(dist[nextEdge.end] > newCost) {
                    dist[nextEdge.end] = newCost;
                    pq.add(new Node(nextEdge.end, newCost));
                }
            }
        }
    }

    static class Node implements Comparable<Node>{
        int vertex;
        int cost;

        Node(int vertex, int cost) {
            this.vertex = vertex;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }
}

```