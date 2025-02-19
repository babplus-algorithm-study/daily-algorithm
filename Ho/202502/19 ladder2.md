```java
import java.util.*;
import java.io.*;

public class Solution {
    static int T,N,ans;
    static int realAns = 0;
    static int[][] grid =new int[100][100];
    static boolean[][] visited;
    static int[] drs = { 0, 0,1};
    static int[] dcs = {-1, 1,0};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for(int t = 1; t <= 10; t++) {
            T = Integer.parseInt(br.readLine());
            ans = 123456789;
            realAns = 0;
            for(int i =0; i < 100; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());

                for(int j = 0; j < 100; j++) {
                    grid[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            for(int i =0; i < 100; i++) {
                visited = new boolean[100][100];
                if(grid[0][i] == 0) continue;
                visited[0][i] = true;
                dfs(0,i,1,i);
            }

            sb.append("#").append(t).append(" ").append(realAns).append("\n");
        }
        System.out.print(sb);
    }


    private static void dfs(int r, int c,int cnt,int start) {
        if(cnt > ans) return;
        if(r == 99) {
            realAns = start;
            ans = cnt;

            return;
        }

        boolean flag = false;

        for(int i = 0; i < 3; i++) {
            if(flag) continue;

            int nr = r + drs[i];
            int nc = c + dcs[i];

            if(inRange(nr,nc) && !visited[nr][nc] && grid[nr][nc] != 0) {
                visited[nr][nc] = true;
                if (i != 2) flag = true;
                dfs(nr,nc,cnt + 1,start);
                visited[nr][nc] = false;
            }
        }
    }

    private static boolean inRange(int r, int c) {
        return c >= 0 && c < 100;
    }


}

```