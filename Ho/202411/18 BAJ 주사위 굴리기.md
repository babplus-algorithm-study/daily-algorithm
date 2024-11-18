```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int N,M;
    static int[][] grid;
    static int[] dice = {0, 0, 0, 0, 0, 0};
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        int curR = Integer.parseInt(st.nextToken());
        int curC = Integer.parseInt(st.nextToken());
        int count = Integer.parseInt(st.nextToken());

        // 세로 크기 N, 가로크기 M
        grid = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j <M ; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        st = new StringTokenizer(br.readLine());
        int[] drs = {0, 0, -1, 1};
        int[] dcs = {1, -1, 0, 0};
        for(int i = 0; i < count; i++) {
            // count에 맞게 주사위 움직이기
            int dir = Integer.parseInt(st.nextToken()) - 1;

            int nR = curR + drs[dir];
            int nC = curC + dcs[dir];

            if(inRange(nR,nC)) {
                curR = nR;
                curC = nC;
                move(curR, curC, dir);
            }
        }
        System.out.print(sb.toString());
    }

    public static void move(int r, int c, int dir) {
        int[] copy = Arrays.copyOf(dice, dice.length);

        switch (dir) {
            case 0:
                //동쪽
                dice[1] = copy[5];
                dice[3] = copy[4];
                dice[5] = copy[3];
                dice[4] = copy[1];
                break;
            case 1:
                // 서쪽
                dice[1] = copy[4];
                dice[3] = copy[5];
                dice[4] = copy[3];
                dice[5] = copy[1];

                break;
            case 2:
                // 북쪽
                dice[0] = copy[3];
                dice[1] = copy[0];
                dice[2] = copy[1];
                dice[3] = copy[2];
                break;
            case 3:
                // 남쪽
                dice[0] = copy[1];
                dice[1] = copy[2];
                dice[2] = copy[3];
                dice[3] = copy[0];
                break;
            default:
                // 동서남북의 경우가 아닌 경우
                break;
        }

        if(grid[r][c] != 0) {
            dice[1] = grid[r][c];
            grid[r][c] = 0;
        }
        else{
            grid[r][c] = dice[1];
        }
        sb.append(dice[3] + "\n");
    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < M;
    }
}

```