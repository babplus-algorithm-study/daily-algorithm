```java
package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class P21610 {
    static int N, M;
    static int[][] grid;
    static Queue<Pair> q = new LinkedList<>();
    static boolean[][] used;

    static class Pair {
        int r;
        int c;

        Pair(int r, int c) {
            this.r = r;
            this.c = c;

        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        grid = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            for (int j = 0; j < N; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        q.add(new Pair(N - 1, 0));
        q.add(new Pair(N - 2, 0));
        q.add(new Pair(N - 1, 1));
        q.add(new Pair(N - 2, 1));

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());

            int dir = Integer.parseInt(st.nextToken()) - 1;
            int cnt = Integer.parseInt(st.nextToken());

            used = new boolean[N][N];
            move(dir, cnt);
            copy();
            makeCloud();
        }
        System.out.println(sumAmount());
    }

    public static void move(int dir, int cnt) {

        int[] drs = {0, -1, -1, -1, 0, 1, 1, 1};
        int[] dcs = {-1, -1, 0, 1, 1, 1, 0, -1};

        for (int i = 0; i < q.size(); i++) {
            Pair curPair = q.poll();

            curPair.r = (curPair.r + drs[dir] * cnt) % N;
            curPair.c = (curPair.c + dcs[dir] * cnt) % N;

            if(curPair.r < 0) curPair.r += N;
            if(curPair.c < 0) curPair.c += N;

            q.add(curPair);
            grid[curPair.r][curPair.c]++;
            used[curPair.r][curPair.c] = true;
        }
    }

    public static void copy() {
        int[] drs = {-1, -1, 1, 1};
        int[] dcs = {1, -1, 1, -1};

        while(!q.isEmpty()) {
            Pair curPair = q.poll();

            for(int i = 0; i < 4; i++) {
                int nR = curPair.r + drs[i];
                int nC = curPair.c + dcs[i];

                if(inRange(nR,nC)) {
                    //물 복사 가능한지 체크
                    if(grid[nR][nC] > 0){
                        grid[curPair.r][curPair.c]++;
                    }
                }
            }
        }


    }

    public static boolean inRange(int r, int c) {
        return r >= 0 && r < N && c >= 0 && c < N;
    }

    public static void makeCloud() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(used[i][j]) continue;
                if(grid[i][j] > 1) {
                    grid[i][j] -= 2;

                    q.add(new Pair(i, j));
                }
            }
        }
    }

    public static int sumAmount() {
        int sum = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sum += grid[i][j];
                }
            }
        return sum;
    }

}

```