```java
package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class P20057 {
    static int[][] grid;
    static int answer;
    static int N;
    static boolean[][] visited;
    static int cnt = 0;
    static int size = 1;
    static int dir = 0;

    // x -> y 로 이동하면 y 모래가 날라간다.
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        answer = 0;
        grid = new int[N][N];
        visited = new boolean[N][N];

        for(int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        tornado();
    }

    public static void tornado() {
        int r = N/2;
        int c = N/2;

        while(true) {

            if(r == 0 && c == 0) {
                return;
            }
            int[] pos = move(r, c);
            r = pos[0];
            c = pos[1];
        }
    }

    public static void scatter(int r, int c, int dir) {
        int[] drs;
        int[] dcs;
        int[] per;

        if(dir == 0) {
            drs = new int[]{-2, 2, -1, -1, -1, 0, 1, 1, 1};
            dcs = new int[]{0, 0, -1, 0, 1, -2, -1, 0, 1};
            per = new int[]{2, 2, 10, 7, 1, 5, 10, 7, 1};

        }

        else if(dir == 1) {
            drs = new int[]{0, 0, 0, 0, -1, -1, 1, 1, 2};
            dcs = new int[]{-2, -1, 1, 2, -1, 1, -1, 1, 0};
            per = new int[]{2, 7, 7, 2, 1, 1, 10, 10, 5};
        }

        else if(dir == 2) {
            drs = new int[]{-2, -1, 1, 2, -1, 1, -1, 1, 0};
            dcs = new int[]{0, 0, 0, 0, -1, -1, 1, 1, 2};
            per = new int[]{2, 7, 7, 2, 1, 1, 10, 10, 5};

        }
        else {
            drs = new int[]{0, 0, 0, 0, 1, 1, -1, -1, -2};
            dcs = new int[]{-2, -1, 1, 2, -1, 1, -1, 1, 0};
            per = new int[]{2, 7, 7, 2, 1, 1, 10, 10, 5};
        }


        // 알파로 보낼거 찾기
        int curSand = grid[r][c];
        int moveAmount = 0;

        for(int i = 0; i < drs.length; i++) {
            int nextR = r + drs[i];
            int nextC = c + dcs[i];


            int curMove = (int) (curSand * (double)(per[i]) / (double) 100);
            moveAmount += curMove;

            if(!inRange(nextR,nextC)) {
                // 소멸되는 모래
                answer += curMove;
            }
            else{
                grid[nextR][nextC] += curMove;
            }
        }
        // 이동하고 남은 모래만큼 알파 자리로
        int remainderSand = curSand - moveAmount;

        int[] dr = {0,1,0,-1};
        int[] dc = {-1,0,1,0};

        int nextR = r + dr[dir];
        int nextC = c + dc[dir];

        if(!inRange(nextR,nextC)) {
            answer += remainderSand;
            grid[r][c] = 0;
            return;
        }

        grid[nextR][nextC] += remainderSand;
        grid[r][c] = 0;
    }

    public static int[] move(int r, int c) {
        int[] drs = {0,1,0,-1};
        int[] dcs = {-1,0,1,0};

        dir = dir % 4;
        int nextR = r;
        int nextC = c;

        for(int i = 0; i < size; i++) {
            nextR = nextR + (drs[dir]);
            nextC = nextC + (dcs[dir]);

            System.out.println(nextR + " "+nextC);
            System.out.println(dir);
            for(int k = 0; k < N; k++) {
                for(int j = 0; j < N; j++) {
                    System.out.print(grid[k][j] +" ");
                }
                System.out.println();
            }
            System.out.println();

            if(!inRange(nextR,nextC)) {
                scatter(nextR, nextC + 1, dir);

                return new int[]{nextR, nextC +1};
            }
            scatter(nextR, nextC, dir);
        }

        cnt++;
        dir++;

        if(cnt % 2 == 0) {
            size++;
        }
        return new int[] { nextR, nextC };
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < N;
    }

}

```