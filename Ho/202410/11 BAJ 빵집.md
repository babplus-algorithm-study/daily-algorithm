```java
package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P3109 {
    static boolean[][] grid;
    static int R;
    static int C;

    static boolean[][] visited;
    static int answer = 0;
    static boolean[] check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        grid = new boolean[R][C];
        visited = new boolean[R][C];
        check = new boolean[R];

        for(int i = 0; i < R; i++) {
            String line = br.readLine();
            char[] a =  line.toCharArray();
            for(int j = 0; j < C; j++) {
                if(a[j] == 'x') grid[i][j] = false;
                else{
                    grid[i][j] = true;
                }
            }
        }
        for(int i = 0; i < R; i++) {
            dfs(i, 0, i);
        }
        System.out.println(answer);
    }

    public static boolean dfs(int r, int c, int uniqueKey) {
        if(c == C-1) {
            check[uniqueKey] = true;
            answer++;
            return true;
        }

        visited[r][c] = true;

        int[] drs = {-1, 0, 1};
        int[] dcs = {1, 1, 1};

        for(int dir = 0; dir < 3; dir++) {
            int nextR = r + drs[dir];
            int nextC = c + dcs[dir];

            if (canGo(nextR, nextC, uniqueKey)) {
                visited[nextR][nextC] = true;
                if(dfs(nextR, nextC, uniqueKey)) return true;
            }
        }
        return false;
    }

    public static boolean inRange(int r, int c) {
        return r >=0 && r < R && c >= 0 && c < C;
    }

    public static boolean canGo(int r, int c,int uKey) {
        if(!inRange(r,c)) return false;
        if(visited[r][c]) return false;
        if(!grid[r][c]) return false;
        if(check[uKey]) return false;
        return true;
    }

}

```