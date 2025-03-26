```java
import java.util.*;
import java.io.*;

public class Main {
    static final int OFFSET = (int) 1e9;
    static int N,M;
    static long minCost, maxCost;
    static final String YES = "YES";
    static final String NO = "NO";

    static ArrayList<Node>[] nodes;
    static Node[] minNodes;
    static Node[] maxNodes;

    static int[] minGroups;
    static int[] maxGroups;
    static HashSet<Integer> minSet = new HashSet<>();
    static HashSet<Integer> maxSet = new HashSet<>();
    static int[] ans;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        nodes = new ArrayList[N+1];
        minNodes = new Node[M];
        maxNodes = new Node[M];

        minGroups = new int[N + 1];
        maxGroups = new int[N + 1];

        for (int i = 0; i < N+1; i++) {
            nodes[i] = new ArrayList<>();

            minGroups[i] = i;
            maxGroups[i] = i;
        }

        for(int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken())  + OFFSET;

            nodes[a].add(new Node(b, a, c,i+1));
            nodes[b].add(new Node(a, b, c,i+1));

            minNodes[i] = new Node(a, b, c,i+1);
            maxNodes[i] = new Node(a, b, c,i+1);
        }

        Arrays.sort(minNodes);

        StringBuilder sb = new StringBuilder();

        if(N > M) {
            // MMST가 존재할 수 없는 경우
            sb.append(NO);
        }
        else {
            //최소 구하기
            minCost = 0;
            maxCost = 0;
            int idx = M - 1;
            for(int i = 0; i < M ; i++ ) {
                // 연결했을 때 사이클이 발생하지 않는다면 연결
                Node curNode = minNodes[i];

                if(find(curNode.to, 0) != find(curNode.from, 0)) {
                    union(curNode.from, curNode.to, 0);

                    minCost += curNode.cost;
                    minSet.add(curNode.num);
                }

                curNode = minNodes[idx--];

                if (find(curNode.to,1) != find(curNode.from, 1)) {
                    union(curNode.from, curNode.to , 1);
                    maxCost += curNode.cost;
                    maxSet.add(curNode.num);
                }
            }
            // min,max가 아닌 트리를 만들어보자

            if(minCost == maxCost) {
                sb.append(NO);
            }
            else{
                // 중간 간선들 찾아보기
                boolean flag = true;
                for(int i = 0; i < M; i++) {
                    int idx1 =  minNodes[i].num;
                    if(minSet.contains(idx1) && maxSet.contains(idx1)) continue;

                    if(minSet.contains(idx1) || maxSet.contains(idx1)) {
                        if(canBuildWithout(idx1)) {
                            //MMST 인경우
                            sb.append(YES +"\n");
                            for(int j = 0; j < N - 1; j++) {
                                sb.append(ans[j] + " ");
                            }
                            flag = false;
                            break;
                        }
                    }
                }
                if(flag) {
                    sb.append(NO);
                }
            }

        }
        System.out.println(sb);
    }

    static private boolean canBuildWithout(int idx) {
        // i번 간선을 제외하고 연결할 수 있는지
        minGroups = new int[N+1];
        ans = new int[N-1];

        for(int i = 0 ; i <= N; i++) {
            minGroups[i] = i;
        }
        
        long cost = 0;
        int cnt = 0;

        for(int i = 0 ; i < M; i++) {
            if(cnt == N - 1) break;
            Node curNode = minNodes[i];

            if(curNode.num == idx) continue;

            if(find(curNode.to, 0) != find(curNode.from, 0)) {
                union(curNode.from, curNode.to, 0);

                cost += curNode.cost;
                ans[cnt] = curNode.num;
                cnt++;
            }
        }

        return cnt == N - 1 && cost > minCost && cost < maxCost;
    }

    static private int find(int x, int cmd) {
        if(cmd == 0) {
            if(minGroups[x] != x) return minGroups[x] = find(minGroups[x], cmd);
            return minGroups[x];
        }

        else{
            if(maxGroups[x] != x) return maxGroups[x] = find(maxGroups[x],cmd);
            return maxGroups[x];
        }

    }

    static private void union(int a, int b, int cmd) {
        a = find(a, cmd);
        b = find(b, cmd);

        if(a > b) {
            int temp = a;
            a = b;
            b = temp;
        }

        if(cmd == 0) minGroups[b] = a;
        else maxGroups[b] = a;

    }

    static class Node implements Comparable<Node> {
        int cost;
        int to;
        int from;
        int num;

        Node(int to,int from, int cost, int num) {
            this.to = to;
            this.from = from;
            this.cost = cost;
            this.num = num;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }



}

```