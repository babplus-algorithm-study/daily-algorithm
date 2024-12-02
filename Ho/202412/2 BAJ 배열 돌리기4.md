```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class P17406 {
    static int N,M,K;
    static int[][] grid;
    static boolean[] used;
    static Op[] ops;
    static int ans = (int) 1e9;

    static class Op {
        int r;
        int c;
        int s;

        Op(int r, int c, int s) {
            this.r = r;
            this.c = c;
            this.s = s;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        grid = new int[N][M];
        used = new boolean[K];
        ops = new Op[K];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());

            int r = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            int s = Integer.parseInt(st.nextToken());

            ops[i] = new Op(r, c, s);
            // 회전연산을 임의로 실행하고 최소 값을 찾는 문제
        }
        simulate(0,0,grid);
        System.out.println(ans);
    }

    //시뮬돌리면서 체크하기
    public static void simulate(int depth, int usedCnt, int[][] newGrid) {
        if(depth == K){
            if(usedCnt == K) {
                //배열 A의 최소 값 찾기
                sumRow(newGrid);
            }
            return;
        }

        for(int i = 0; i < K; i++) {
            if(used[i]) continue;

            int[][] tempGrid = Arrays.stream(newGrid)
                    .map(arr -> arr.clone())
                    .toArray(int[][]::new);

            int r = ops[i].r;
            int c = ops[i].c;
            int s = ops[i].s;

            int cnt = s;
            for (int j = 0; j < s; j++) {
                rotate(r-s+j,c-s+j,((cnt - j) * 2) + 1 ,tempGrid);
            }

            used[i] = true;
            simulate(depth + 1, usedCnt + 1,tempGrid);
            used[i] = false;
        }

    }

    public static void sumRow(int[][] newGrid) {
        for(int i = 0; i < N; i++) {
            int curSum = 0;
            for(int j = 0; j < M; j++) {
                curSum += newGrid[i][j];
            }
            ans = Math.min(curSum,ans);
        }
    }

    // 한번 돌리고 백트래킹하면 다시 이전으로 돌아와야한다.
    public static void rotate(int r,int c,int size, int[][] newGrid) {
        int temp = newGrid[r + 1][c];

        // 아래로
        for(int i = r + 1; i < r + size - 1; i++) {
            newGrid[i][c] = newGrid[i + 1][c];
        }

        // 우측
        for(int i = c; i < c + size -1; i++) {
            newGrid[r + size - 1][i] = newGrid[r + size - 1][i + 1];
        }

        //위로
        for(int i = r + size -1; i > r; i--) {
            newGrid[i][c + size - 1] = newGrid[i - 1][c + size - 1];
        }

        // 좌측
        for(int i = c + size - 1; i > c; i--) {
            newGrid[r][i] = newGrid[r][i - 1];
        }

        newGrid[r][c] = temp;

    }
}

```