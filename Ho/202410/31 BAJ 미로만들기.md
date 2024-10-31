```java
package baekjoon;

import java.util.*;
import java.io.*;

public class P2665 {
    static int N,ans;
    static int[][] grid;
    static boolean[][][] visited;

    public static void main(String[] args) throws IOException{
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

         N = Integer.parseInt(br.readLine());

         grid = new int[N][N];
         visited = new boolean[2500][N][N];

         for(int i =0; i < N; i++) {
             String line = br.readLine();
             for(int j = 0; j < N; j++) {
                 grid[i][j] = line.charAt(j) - '0';
             }
         }

         ans = 2501;
         bfs();
         System.out.println(ans);
    }

    public static void bfs() {
        Queue<Node> q = new LinkedList<>();
        q.add(new Node(0, 0, 0));
        visited[0][0][0] = true;

        while(!q.isEmpty()) {
            Node cur = q.poll();

            int b = cur.b;
            int r = cur.r;
            int c = cur.c;
            if(b > ans) continue;
            if(r == N-1 && c == N-1) {
                ans = Math.min(ans,b);
                continue;
            }

            int[] drs = {1, 0, 0, -1};
            int[] dcs = {0, 1, -1, 0};

            for(int i = 0; i < 4; i++) {
                int nR = r + drs[i];
                int nC = c + dcs[i];

                if(canGo(nR, nC, b)) {
                    if (isBlack(nR, nC)) {
                        q.add(new Node(nR, nC, b + 1));
                        visited[b+1][nR][nC] = true;
                    }
                    else{
                        q.add(new Node(nR, nC, b));
                        visited[b][nR][nC] = true;
                    }
                }
            }
        }
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < N;
    }

    public static boolean isBlack(int r, int c) {
        if(grid[r][c] == 1) return false;
        return true;
    }

    public static boolean canGo(int r, int c,int b) {
        if(b > 2499) return false;
        if(!inRange(r, c)) return false;
        if(isBlack(r, c)) {
            if(visited[b+1][r][c]) return false;
            return true;
        }
        if(visited[b][r][c]) return false;
        return true;
    }

    static class Node {
        int r, c, b;

        Node(int r, int c, int b) {
            this.r = r;
            this.c = c;
            this.b = b;
        }
    }
}
```