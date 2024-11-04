```java
public class Main2 {

    static int[][] map;
    static int[] di = {-1, 0, 1, 0};
    static int[] dj = {0, -1, 0, 1};
    static int N;
    static int M;
    public static void main(String[] args) throws Exception {
        N = read();
        M = read();

        map = new int[N + 2][M + 2];

        int si = read() + 1;
        int sj = read() + 1;
        int dir = read();
        if(dir == 1) dir = 3;
        else if(dir == 3) dir = 1;

        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= M; j++) {
                // 0이면 못감 1이면 청소 안됨 2면 벽 3이면 청소됨
                map[i][j] = (read() + 1);
            }
        }

        int ans = 0;

        while(true) {
            if(check(si, sj)) {
                System.out.println(ans);
                return;
            }

            if(map[si][sj] == 1) {
                ans++;
                map[si][sj] = 3;
            }
            // 주변 탐색

            boolean b = true;
            for(int i = 1; i <= 4; i++) {
                int dd = (dir + i) % 4;
                // 주변 중 가장 먼저 더러운 부분 만나면? 거기로 이동
               if(map[si + di[dd]][sj + dj[dd]] == 1) {
                   dir = dd;
                   si += di[dd];
                   sj += dj[dd];
                   b = false;
                   break;
               }
            }

            // 더러운 부분이 없다면?
            if(b) {
                si -= di[dir];
                sj -= dj[dir];
            }


        }


    }


    public static boolean check(int i, int j) {
        return map[i][j] == 2;
    }

    private static int read() throws Exception {
        int d, o = System.in.read() & 15;
        while ((d = System.in.read()) > 32)
            o = (o << 3) + (o << 1) + (d & 15);
        return o;
    }
}

```
