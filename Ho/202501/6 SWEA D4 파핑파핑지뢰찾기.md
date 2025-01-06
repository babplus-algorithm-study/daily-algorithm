```java
package swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class FindMine {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for(int t = 1; t <= T; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());

            int[][] grid = new int[N][N];
            boolean[][] visited = new boolean[N][N];

            for(int i =0; i < N; i++) {
                String gridString = br.readLine();

                for(int j = 0; j < N; j++) {
                    if(gridString.charAt(j) == '.') {
                        grid[i][j] = -1;
                    }
                    else{
                        visited[i][j] = true;
                        grid[i][j] = -9;
                    }
                }
            }

            int ans = 0;

            for(int i =0; i < N; i++) {
                for(int j =0; j < N; j++) {
                    if(grid[i][j] != -9 && !visited[i][j]) {
                        if(!detectMind(i,j,grid)) {
                            //8 방향에 지뢰가 없는 경우 누르기
                            ans++;
                            spreadZero(i,j,grid,visited,0);
                        }
                    }
                }
            }

            for(int i =0; i < N; i++) {
                for(int j =0; j < N; j++) {
                    if(!visited[i][j]) ans++;
                }
            }

            sb.append("#" + t +" " + ans +"\n");

        }
        System.out.println(sb.toString());

    }

    public static boolean detectMind(int r, int c, int[][] grid) {
        int[] drs = {-1, -1, 0, 1, 1, 1, 0, -1};
        int[] dcs = {0, 1, 1, 1, 0, -1, -1, -1};

        for(int i =0; i < 8; i++) {
            int nR = r + drs[i];
            int nC = c + dcs[i];

            if (inRange(nR, nC, grid.length)) {
                if(grid[nR][nC] == -9) {
                    return true;
                }
            }
        }
        return false;
    }

    //내가 0인 경우 전파 가능
    public static void spreadZero(int r, int c, int[][] grid, boolean[][] visited, int depth) {
        int[] drs = {-1, -1, 0, 1, 1, 1, 0, -1};
        int[] dcs = {0, 1, 1, 1, 0, -1, -1, -1};

        visited[r][c] = true;

        for(int i =0; i < 8; i++) {
            int nR = r + drs[i];
            int nC = c + dcs[i];

            if (inRange(nR, nC, grid.length)) {
                if(grid[nR][nC] == -9 || visited[nR][nC]) {
                    continue;
                }
                visited[nR][nC] = true;
                if(!detectMind(nR, nC, grid)) {
                    spreadZero(nR, nC, grid, visited,0);
                }
            }
        }
    }

    public static boolean inRange(int r, int c, int n) {
        return r >= 0 && r < n && c >= 0 && c< n;
    }
}

```