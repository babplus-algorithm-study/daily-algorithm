```java
import java.util.*;
import java.io.*;

class Solution {
    int[][] dist;
    ArrayList<Node>[] graph;
    
    class Node implements Comparable<Node> {
        int dist;
        int vertex;
        
        public Node(int dist, int vertex) {
            this.dist = dist;
            this.vertex = vertex;
        }
        
        @Override
        public int compareTo(Node o) {
            return this.dist - o.dist;
        }
    }
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = (int)1e8;
        int size = n + 1;
        
        dist = new int[size][size];
        graph = new ArrayList[size];
        
        //인접리스트를 초기화
        for(int i = 1; i < size; i++) {
            graph[i] = new ArrayList<>();
            for(int j = 1; j < size; j++) {
                dist[i][j] = (int) 1e8;
            }
        }
        
        //경로 초기화
        for(int i = 0; i < fares.length; i++) {
            int v1 = fares[i][0];
            int v2 = fares[i][1];
            
            graph[v1].add(new Node(fares[i][2], v2));
            graph[v2].add(new Node(fares[i][2], v1));
        }
        
        getMinCost(s);
        // 여기서 정점 하나씩 이동하면서 최소 요금인 경우 찾기
        for(int v = 1; v < size; v++) {
            // v 정점까지는 합승해서 이동하고 각자 이동하기
            getMinCost(v);
            answer = Math.min(answer, dist[v][a] + dist[v][b] + dist[s][v]);
        }

        
        return answer;
    }
    
    public void getMinCost(int startVertex) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        
        pq.add(new Node(0, startVertex));
        dist[startVertex][startVertex] = 0;
        
        while(pq.size() > 0) {
            int curVertex = pq.peek().vertex;
            int curVerDist = pq.peek().dist;
            pq.poll();
            
            if(dist[startVertex][curVertex] != curVerDist) {
                continue;
            }
            
            for(int i = 0; i < graph[curVertex].size(); i++) {
                int nextVertex = graph[curVertex].get(i).vertex;
                int nextVertexDist = graph[curVertex].get(i).dist;
                
                int newDist = nextVertexDist + dist[startVertex][curVertex];
                
                if(newDist <  dist[startVertex][nextVertex]) {
                    dist[startVertex][nextVertex] = newDist;
                    pq.add(new Node(newDist, nextVertex));
                }
            }
        }
    }
}
```

PRS=$(gh pr list --state open --base main --json number,title --jq '.[] | select(.title | startswith("[" + "'"$TODAY"'" + "]")) | .number')
PRS=$(gh pr list --state open --base main --json number,title --jq '.[]) | select(.title | startswith("[" + "'"$TODAY"'" + "]")) | .number')