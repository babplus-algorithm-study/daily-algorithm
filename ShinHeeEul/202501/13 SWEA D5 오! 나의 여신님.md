```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Solution
{
    // 길 : 1, 돌 : 0, 악마 : 2, 시작 : 3, 도착 : 4
    static int[][] map;
    static int[] di = {1,-1,0,0};
    static int[] dj = {0,0,1,-1};
    static int N;
    static int M;
    static boolean[][] visited;
    static Queue<Node> devilQueue;

    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());


        StringBuilder sb = new StringBuilder();

        for(int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            map = new int[N + 2][M + 2];
            visited = new boolean[N + 2][M + 2];

            int[] start = new int[2];
            devilQueue = new LinkedList<>();

            for(int i = 1; i <= N; i++) {
                String s = br.readLine();
                for(int j = 1; j <= M; j++) {
                    char a = s.charAt(j-1);

                    if(a == 'D') {
                        map[i][j] = 4;
                    } else if(a == 'S') {
                        start[0] = i;
                        start[1] = j;
                        map[i][j] = 3;
                    } else if(a == '*') {
                        map[i][j] = 2;
                        devilQueue.add(new Node(i,j,0));
                    } else if(a == '.') {
                        map[i][j] = 1;
                    }

                }
            }
            int a = bfs(start[0], start[1]);
            sb.append("#").append(t).append(" ").append(a == -1 ? "GAME OVER" : a).append("\n");
        }
        System.out.println(sb);


    }

    public static int bfs(int si, int sj) {

        Queue<Node> queue = new LinkedList<>();

        queue.add(new Node(si, sj, 0));
        visited[si][sj] = true;
        // before count
        // 이전 카운트에 비해 달라졌으면? 그 전에건 끝
        // map을 업데이트

        int beforeCount = -1;

        while(!queue.isEmpty()) {

            Node node = queue.poll();

            int ni = node.i;
            int nj = node.j;
            int nc = node.count;

            if(map[ni][nj] == 4) return nc;
            if(map[ni][nj] == 2) continue;

            if(beforeCount < nc) {
                update(nc + 1);
                beforeCount = nc;
            }


            for(int i = 0; i < 4; i++) {
                int ii = ni + di[i];
                int jj = nj + dj[i];
                if(check(ii,jj, nc + 1)) {
                    visited[ii][jj] = true;
                    queue.add(new Node(ii, jj, nc + 1));
                }
            }
        }

        return -1;
    }

    public static void update(int count) {

        while(!devilQueue.isEmpty()) {
            Node node = devilQueue.poll();

            int ni = node.i;
            int nj = node.j;
            int nc= node.count;

            if(nc == count) {
                devilQueue.add(node);
                return;
            }


            for(int i = 0; i < 4; i++) {
                int ii = ni + di[i];
                int jj = nj + dj[i];
                if(devilCheck(ii,jj, nc + 1)) {
                    map[ii][jj] = 2;
                    devilQueue.add(new Node(ii, jj, nc + 1));
                }
            }
        }

    }

    public static boolean devilCheck(int i, int j, int count) {
        if(map[i][j] == 0 || map[i][j] == 2 || map[i][j] == 4) return false;

        return true;
    }

    public static boolean check(int i, int j, int count) {
        if(map[i][j] != 1 && map[i][j] != 4) return false;
        if(visited[i][j]) return false;

        return true;
    }

    public static class Node {
        int i;
        int j;
        int count;

        public Node(int i, int j, int count) {
            this.i = i;
            this.j = j;
            this.count = count;
        }
    }
}
```
